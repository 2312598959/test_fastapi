from fastapi import FastAPI, Request

api_test = FastAPI()


@api_test.get("/")
def read_root():

    return "hh"
