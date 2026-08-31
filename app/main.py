from fastapi import FastAPI
from app.routers.users import router as users_router
from app.routers.auth import router as auth_token
from app.routers.product import router as product_router
from app.routers.order import router as order_router
from app.database import Base, engine
from app.models.user import User
from app.models.product import Product


app = FastAPI(
    title='BotFlow API',
    version='0.1.0',
    description='API para automação de pagamentos e bots do Telegram;'
)

app.include_router(users_router)
app.include_router(auth_token)
app.include_router(product_router)
app.include_router(order_router)

Base.metadata.create_all(bind=engine)


@app.get('/health')
def health():
    ...

@app.get('/about')
def about():
    ...

