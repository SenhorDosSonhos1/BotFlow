from fastapi import APIRouter, HTTPException,Depends

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.models.user import User

from sqlalchemy.orm import Session
from app.database import get_db

from app.security.password import get_password_hash
from app.security.jwt import get_current_user


router = APIRouter(
    prefix='/users', #Coloca a rota padrão(pai) pra todas as rotas
    tags=['Users'] # Organiza em tipos no Swagger
)


@router.post('/', status_code=201, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter_by(email = user.email).first():
        raise HTTPException(
            status_code=404,
            detail='Nome de usuario ou email já existe no sistema.'
        )

    password_hash = get_password_hash(user.password)
    user = User(username = user.username, email = user.email, password_hash = password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get('/', response_model=list[UserResponse])
def list_all_users(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(User).all()

@router.put('/{user_id}', response_model=UserResponse, status_code=200)
def update_user(
    user_id: int, update_data: UserUpdate,
    db: Session = Depends(get_db), current_user = Depends(get_current_user)
    ):
    user = db.query(User).filter_by(id = user_id).first()
    if user is None:
        raise HTTPException(
            status_code=404, 
            detail='Usuário não encontrado'
        )
    
    if user.id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail='Você não tem permissão para realizar esta operação.'
        )
    
    user.username = update_data.username
    user.email = update_data.email
        
    db.commit()
    db.refresh(user)

    return user 

@router.delete('/{user_id}', status_code=200)
def delete_user(
    user_id: int, db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ): 
    user = db.query(User).filter_by(id = user_id).first()
    if user is None:
        raise HTTPException (
            status_code=404,
            detail='Usuário não encontrado'
        )  
    if user.id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail='Você não tem permissão para realizar esta operação.'
        )
    db.delete(user)
    db.commit()
    return {'message': 'Usuario deletado com sucesso.'}

@router.get('/{user_id}', response_model=UserResponse, status_code=200)
def get_user(
    user_id: int, db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    user = db.query(User).filter_by(id = user_id).first()

    if user is not None:
        return user 
    
    raise HTTPException (
        status_code=404,
        detail='Usuario não encontrado'
    ) 
