from fastapi import FastAPI

api_test = FastAPI()
@api_test .get("/")
@api_test .get("/invoke")
@api_test.post("/invoke")
async def invoke():
    print('hello')
    return {"Hello": "World"}
