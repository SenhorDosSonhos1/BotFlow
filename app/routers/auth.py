from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.models.user import User
from app.database import get_db
from sqlalchemy.orm import Session

from app.security.password import verify_password

from app.security.jwt import create_access_token
from app.schemas.token import Token


router = APIRouter(
    prefix='/token',
    tags=["JWT"]
)

@router.post('', response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
    ):
    user = db.query(User).filter_by(email = form_data.username).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail='Credenciais incorretas'
        )

    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Credenciais incorretas"
        )

    #Enviando o subject pro header
    access_token = create_access_token({'sub': user.email})
    return {
        'access_token': access_token,
        'token_type': 'Bearer'
    }

