from fastapi import FastAPI
from api.financial_api import router

app = FastAPI(title="Financial AI Platform")
app.include_router(router)
