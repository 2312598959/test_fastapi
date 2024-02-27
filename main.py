from fastapi import FastAPI, Request
import uvicorn

api_test = FastAPI()


@api_test.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])

def test():

    return "hh"


