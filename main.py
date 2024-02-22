
from fastapi import FastAPI

api_test = FastAPI()

@api_test.get("/")
def read_root():
    return {"Hello": "World"}
