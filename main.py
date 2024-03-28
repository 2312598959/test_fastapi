from loguru import logger
from fastapi import FastAPI, Request

api_test = FastAPI()


@api_test.post("/invoke")
async def invoke(incoming_request: Request):
    # Show version
    logger.info("1.0")
    print("access_key_id")
    # Check incoming request header
    logger.info(f"Request header -> {incoming_request.headers}")
    logger.info("2.0")
    # 异步方式获取请求体
    body = await incoming_request.body()

    print(body)
    # Get incoming request body
    payload = await incoming_request.json()
    logger.info(f"Request body -> {payload}")
    logger.info("3.0")
    oss_endpoint = payload["oss_endpoint"]
    oss_bucket = payload["oss_bucket"]
    validate_config_excel = payload["validate_config"]
    oss_error_folder = payload["oss_error_folder"]
    oss_archive_folder = payload["oss_archive_folder"]
    print(f"payload -> {oss_endpoint}")
    print(f"oss_bucket -> {oss_bucket}")

    print(f"validate_config_excel -> {validate_config_excel}")

    print(f"oss_error_folder -> {oss_error_folder}")

    print(f"oss_archive_folder -> {oss_archive_folder}")

    # Init temporary credentials
    logger.info("4.0")
    access_key_id = (incoming_request.headers["x-fc-access-key-id"],)
    access_key_secret = (incoming_request.headers["x-fc-access-key-secret"],)
    security_token = (incoming_request.headers["x-fc-security-token"],)

    print("access_key_id:", access_key_id)
    print("access_key_secret:", access_key_secret)
    print("security_token:", security_token)
