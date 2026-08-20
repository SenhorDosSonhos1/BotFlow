import os
from jwt import encode, decode

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from fastapi.security import OAuth2PasswordBearer

from fastapi import Depends
from app.database import get_db
from sqlalchemy.orm import Session

from fastapi import HTTPException
from app.models.user import User


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    #exp
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    #Adiciona o xp ao payload
    to_encode.update({'exp': expire})

    #Cria o JWT
    encoded_jwt = encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='token'
)

#Crachá
def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    payload = decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    email = payload.get('sub')

    if email is None:
        raise HTTPException(
            status_code=401,
            detail='Não foi possível validar as credenciais'
        )
    user = db.query(User).filter_by(email = email).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail='Não foi possível validar as credenciais'
        )
    return user