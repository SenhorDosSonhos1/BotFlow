from fastapi import APIRouter, HTTPException,Depends

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.models.user import User

from sqlalchemy.orm import Session
from app.database import get_db


router = APIRouter(
    prefix='/users', #Coloca a rota padrão(pai) pra todas as rotas
    tags=['Users'] # Organiza em tipos no Swagger
)


@router.post('/', status_code=201, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = User(username = user.username, email = user.email, password_hash = user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get('/', response_model=list[UserResponse])
def list_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.put('/{user_id}', response_model=UserResponse, status_code=200)
def update_user(user_id: int, update_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id = user_id).first()

    if user is not None:
        user.username = update_data.username
        user.email = update_data.email
        user.password_hash = update_data.password
        
        db.commit()
        db.refresh(user)
        return user 
    
    raise HTTPException (
        status_code=404,
        detail='Usuario não encontrado'
    ) 

@router.delete('/{user_id}', status_code=200)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id = user_id).first()

    if user is not None:
        db.delete(user)
        db.commit()
        return {'message': 'Usuario deletado com sucesso.'}

    raise HTTPException (
        status_code=404,
        detail='Usuario não encontrado'
    )  

@router.get('/{user_id}', response_model=UserResponse, status_code=200)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id = user_id).first()

    if user is not None:
        return user 
    
    raise HTTPException (
        status_code=404,
        detail='Usuario não encontrado'
    ) 
