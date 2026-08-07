from fastapi import APIRouter, HTTPException
from app.schemas.user import UserSchema, UserDB


router = APIRouter(
    prefix='/users', #Coloca a rota padrão(pai) pra todas as rotas
    tags=['Users'] # Organiza em tipos no Swagger
)

users = []
@router.post('/', status_code=201, response_model=UserSchema)
def create_user(user: UserDB):
    user.id = len(users) + 1
    users.append(user)
    
    return user

@router.get('/')
def list_all_users():
    return users

@router.put('/{username}', response_model=UserSchema)
def update_user(username: str, update_user: str):
    for user in users:
        if user.username == username:
            user.username = update_user
            return user
        
    raise HTTPException (
        status_code=404,
        detail='Usuario não encontrado'
    ) 

@router.delete('/{username}')
def delete_user(username: str):
    for user in users:
        if user.username == username:
            users.remove(user)

            return {'message': 'Usuario removido.'}
        
    raise HTTPException (
        status_code=404,
        detail='Usuario não encontrado'
    )  

@router.get('/{username}', response_model=UserSchema)
def get_user(username: str):
    for user in users:
        if user.username == username:
            return user
        
    raise HTTPException (
        status_code=404,
        detail='Usuario não encontrado'
    ) 
