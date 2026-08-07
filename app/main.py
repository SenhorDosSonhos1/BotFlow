from fastapi import FastAPI, HTTPException
from app.routers.users import router as users_router


app = FastAPI(
    title='BotFlow API',
    version='0.1.0',
    description='API para automação de pagamentos e bots do Telegram;'
)

app.include_router(users_router)

@app.get('/health')
def health():
    ...

@app.get('/about')
def about():
    ...

