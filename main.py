from fastapi import FastAPI, Request

api_test = FastAPI()


@api_test.route("/", methods=["GET", "POST", "PUT", "DELETE"])
async def hello_world(request: Request):
    return {"message": f"Hello!"}
