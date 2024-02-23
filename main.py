from fastapi import FastAPI, Request

api_test = FastAPI()


@api_test.get("/invoke")
def read_root(incoming_request: Request):
    access_key_id = (incoming_request.headers["x-fc-access-key-id"],)
    access_key_secret = incoming_request.headers["x-fc-access-key-secret"]
    security_token = incoming_request.headers["x-fc-security-token"]
    # 将凭证信息添加到返回的字典中，但请注意这在生产环境中通常不安全！
    response_data = {"Hello": "World", 
                    "access_key_id": access_key_id, 
                    "access_key_secret": access_key_secret, 
                    "security_token": security_token}
    
    return response_data
