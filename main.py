from fastapi import FastAPI,Request

REQUEST_ID_HEADER = "sss"
api_test = FastAPI()

@api_test.route("/", defaults={"path": ""})
@api_test.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
async def hello(path):
    rid = request.headers.get(REQUEST_ID_HEADER,'N/A')
    print("FC Invoke Start RequestId: " + rid)
    return {"message": "Hello SharePoint API!"}
