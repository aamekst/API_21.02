from fastapi import FastAPI

from routes import computador_routes #mesmo
from routes import usuarios_routes


app = FastAPI()
app.include_router(computador_routes.router, tags=['computador'])
app.include_router(usuarios_routes.router, tags=['usuarios'])


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)