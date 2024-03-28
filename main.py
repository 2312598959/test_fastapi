from fastapi import FastAPI

api_test = FastAPI()
@api.get("/")
@api.get("/invoke")
@api_test.post("/invoke")
async def invoke():
    return {"Hello": "World"}
