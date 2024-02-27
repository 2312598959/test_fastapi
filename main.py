from fastapi import FastAPI, Request
import uvicorn

api_test = FastAPI()


@api_test.get("/invoke")
def read_root():

    return "hh"


