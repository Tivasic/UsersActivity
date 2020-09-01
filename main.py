from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.requests import Request
import uvicorn
from pathlib import Path
from database.db import SessionLocal
from router import router

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(router)


@app.get("/version")
async def get_version():
    """
    Обработка запроса на версию приложения.
    :return:
    """
    return "Version"


@app.get("/file")
async def download_file():
    base_path = Path()
    file_path = base_path / "Test.xlsx"
    return FileResponse(path=file_path)


def __main():
    port = 8000
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    __main()
