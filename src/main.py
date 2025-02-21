from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from exception_handler import (
    CustomHTTPException,
    ExceptionMiddleware,
    custom_http_exception_handler,
)

app = FastAPI()

app.add_middleware(ExceptionMiddleware)

app.add_exception_handler(CustomHTTPException, custom_http_exception_handler)


# ルートパスへのアクセス
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/exception")
def raise_exception():
    raise Exception("Test Exception")


@app.get("/http_exception")
def raise_http_exception():
    raise HTTPException(status_code=404, detail="Not Found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )
