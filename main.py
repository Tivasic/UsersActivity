from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from database.db import  SQLALCHEMY_DATABASE_URL
from database.db import SessionLocal
from router import router

app = FastAPI()
db = SQLALCHEMY_DATABASE_URL(app)
db.create_all()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(router)
