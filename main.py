"""Main application entrypoint."""


from fastapi import FastAPI


api_test = FastAPI()


@api_test.get("/")
async def hello():
    return {"message": "Hello SharePoint API!"}
