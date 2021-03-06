import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from database.db import SessionLocal
from router import router


app = FastAPI()
app.include_router(router)
templates = Jinja2Templates(directory="templates")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })


@app.get("/version")
async def get_version():
    """
    Обработка запроса на версию приложения.
    :return:
    """
    return "Version"


def __main():
    port = 8000
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    __main()
