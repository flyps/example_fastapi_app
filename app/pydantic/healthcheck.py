from typing import Literal

from pydantic.main import BaseModel


class HealthcheckResponse(BaseModel):
    status: Literal["ok"]
