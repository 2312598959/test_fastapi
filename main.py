from fastapi import FastAPI, Request

api_test = FastAPI()


@api_test.route("/", methods=["GET", "POST", "PUT", "DELETE"])
async def hello_world(request: Request):
    query_params = request.query_params
    # 获取特定查询参数的例子
    name = query_params.get("name", "World")
    
    return {"message": f"Hello, {name}!"}
