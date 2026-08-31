from fastapi import APIRouter, Depends, HTTPException
from app.schemas.order import OrderCreate, OrderResponse

from app.database import get_db
from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.order import Order

from app.security.jwt import get_current_user


router = APIRouter(
    prefix='/orders',
    tags=['Orders']
)

@router.post('', response_model=OrderResponse)
def create_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    product = db.query(Product).filter_by(id = order_data.product_id).first()
    
    if product is None:
        raise HTTPException(
            status_code=404,
            detail='Produto não encontrado'
        )

    elif not product.active:
        raise HTTPException(
            status_code=410,
            detail='Produto não está disponivel'
        )
    
    order = Order(
        user_id = current_user.id,
        product_id = product.id,
        price = product.price,

    )

    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@router.get('', response_model=list[OrderResponse])
def list_orders(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    return db.query(Order).filter_by(user_id = current_user.id).all()

@router.get('/{order_id}', response_model=OrderResponse, status_code=200)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    order = db.query(Order).filter_by(id = order_id).first()

    if order is None:
        raise HTTPException(
            status_code=404,
            detail='Order não foi encontrada'
        )
    
    elif order.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail='Você não tem autorização.'
        )

    return order