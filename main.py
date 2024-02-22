"""Main application entrypoint."""


from fastapi import FastAPI

REQUEST_ID_HEADER = "sss"
api_test = FastAPI()

@api_test.route("/", methods=["GET", "POST", "PUT", "DELETE"])
async def hello():
    rid = request.headers.get(REQUEST_ID_HEADER,'N/A')
    print("FC Invoke Start RequestId: " + rid)
    return {"message": "Hello SharePoint API!"}
