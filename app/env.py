from enum import Enum

import dotenv
from pydantic import BaseSettings, PositiveInt


class LogLevel(str, Enum):
    CRITICAL = "CRITICAL"
    FATAL = "FATAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    WARN = "WARN"
    INFO = "INFO"
    DEBUG = "DEBUG"
    NOTSET = "NOTSET"


class _Env(BaseSettings):
    class Config:
        env_file = dotenv.find_dotenv(raise_error_if_not_found=False)
        env_file_encoding = "utf-8"

    LOG_LEVEL: LogLevel = LogLevel.INFO
    PORT: PositiveInt = 8000


Env = _Env()
