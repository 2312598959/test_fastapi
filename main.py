from fastapi import FastAPI, Request
import uvicorn

api_test = FastAPI()


@api_test.get("/")
def read_root():

    return "hh"

if __name__ == "__main__":
    uvicorn.run(api_test, host="0.0.0.0", port=9000)
