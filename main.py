from fastapi import FastAPI, Request

REQUEST_ID_HEADER = "sss"
api_test = FastAPI()

# 注意：这里假设你确实想用环境变量或者硬编码的方式来获取请求ID的键名
# 如果直接从标准FC头部获取，应改为 'x-fc-request-id'
rid_header_name = os.environ.get("REQUEST_ID_HEADER", "x-fc-request-id")  # 引入os模块以读取环境变量

@api_test.route("/", methods=["GET", "POST", "PUT", "DELETE"])
async def hello_world(request: Request):
    rid = request.headers.get(rid_header_name)
    print("FC Invoke Start RequestId: " + rid)

    return {"message": "Hello, World!"}
