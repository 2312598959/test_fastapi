from fastapi import FastAPI

api_test = FastAPI()

@api_test.post("/invoke")
async def invoke():
    return {"Hello": "World"}
