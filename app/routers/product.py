from fastapi import APIRouter, HTTPException, Depends
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate

from sqlalchemy.orm import Session
from app.database import get_db
from app.models.product import Product



router = APIRouter(
    prefix='/product',
    tags=['Products']
)

@router.post('', response_model=ProductResponse, status_code=201)
def create_product(product_data: ProductCreate ,db: Session = Depends(get_db)):
    product = Product(
        name = product_data.name,
        description = product_data.description,
        price = product_data.price,
        active = product_data.active
    )
    
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@router.get('', response_model=list[ProductResponse], status_code=200)
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.put('/{product_id}', response_model=ProductResponse, status_code=200)
def update_product(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter_by(id = product_id).first()

    if product is not None:
        product.name = product_data.name
        product.description = product_data.description
        product.price = product_data.price 
        product.active = product_data.active

        db.commit()
        db.refresh(product)

        return product
    
    raise HTTPException(
        status_code=404,
        detail="Usuario não encontrado"

    )
@router.delete('/{product_id}', status_code=200)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter_by(id = product_id).first()

    if product is not None:
        db.delete(product)
        db.commit()
        return {'message': 'Produto removido com sucesso.'}

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado."
    )

@router.get('/{product_id}', response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter_by(id = product_id).first()

    if product is not None:
        return product

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado."
    )