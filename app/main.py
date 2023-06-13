import uvicorn
from fastapi import FastAPI

from app.api.healthcheck import healthcheck_router
from app.env import Env

app = FastAPI()

app.include_router(healthcheck_router, tags=["healthcheck"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=Env.PORT, reload=True)
