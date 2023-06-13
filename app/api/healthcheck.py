from fastapi import APIRouter

from app.pydantic.healthcheck import HealthcheckResponse

healthcheck_router = APIRouter()


@healthcheck_router.get("/healthcheck")
def healthcheck() -> HealthcheckResponse:
    return HealthcheckResponse(status="ok")
