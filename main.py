"""Main application entrypoint."""


from fastapi import FastAPI


api_test = FastAPI()

@api_test.route("/", methods=["GET", "POST", "PUT", "DELETE"])
async def hello():
    return {"message": "Hello SharePoint API!"}
