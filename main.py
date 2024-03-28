import uvicorn
import json
from loguru import logger
from fastapi import FastAPI, Request

api_test = FastAPI()


@api_test.get("/")
@api_test.post("/invoke")
async def invoke(incoming_request: Request):
    # Show version
    logger.info("1.0")
    print("access_key_id")
    # Check incoming request header
    logger.info(f"Request header -> {incoming_request.headers}")
    logger.info("2.0")
    # 异步方式获取请求体
    body = await request.body()

    print(body)
    # Get incoming request body
    body = await incoming_request.json()
    logger.info(f"Request body -> {body}")
    logger.info("3.0")
    # Get incoming payload.json
    payload = json.loads(body["payload.json"])
    logger.info(f"payload.json -> {payload}")
    # Init temporary credentials
    logger.info("4.0")
    access_key_id = (incoming_request.headers["x-fc-access-key-id"],)
    access_key_secret = (incoming_request.headers["x-fc-access-key-secret"],)
    security_token = (incoming_request.headers["x-fc-security-token"],)

    print("access_key_id:", access_key_id)
    print("access_key_secret:", access_key_secret)
    print("security_token:", security_token)


if __name__ == "__main__":
    uvicorn.run(api_test, host="0.0.0.0", port=9000)
