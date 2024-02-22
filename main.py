from fastapi import FastAPI,Request

REQUEST_ID_HEADER = "sss"
api_test = FastAPI()

@api_test.route("/", defaults={"path": ""})
@api_test.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def hello_world(path):
        rid = request.headers.get(REQUEST_ID_HEADER)
        print("FC Invoke Start RequestId: " + rid)
        data = request.stream.read()
        print("Path: " + path)
        print("Data: " + str(data))
        print("FC Invoke End RequestId: " + rid)
        return "Hello, World!"
