from fastapi import FastAPI, Request
import uvicorn

api_test = FastAPI()


@api_test.api_route("/", methods=["GET", "POST", "PUT", "DELETE"])

def read_root():

    return "hh"


