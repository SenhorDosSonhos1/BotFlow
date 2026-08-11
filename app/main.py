from fastapi import FastAPI
from app.routers.users import router as users_router

from app.database import Base, engine
from app.models.user import User


app = FastAPI(
    title='BotFlow API',
    version='0.1.0',
    description='API para automação de pagamentos e bots do Telegram;'
)

app.include_router(users_router)

Base.metadata.create_all(bind=engine)


@app.get('/health')
def health():
    ...

@app.get('/about')
def about():
    ...

