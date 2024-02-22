"""Main application entrypoint."""


from fastapi import FastAPI
from flask import request

REQUEST_ID_HEADER = "sss"
api_test = FastAPI()

@api_test.route("/", methods=["GET", "POST", "PUT", "DELETE"])
async def hello(request: Request):
    rid = request.headers.get(REQUEST_ID_HEADER,'N/A')
    print("FC Invoke Start RequestId: " + rid)
    return {"message": "Hello SharePoint API!"}
