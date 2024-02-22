"""Main application entrypoint."""

import json
import time

from fastapi import FastAPI, Request
from loguru import logger


api_test = FastAPI()


@api_test.get("/")
async def hello():
    return {"message": "Hello SharePoint API!"}
