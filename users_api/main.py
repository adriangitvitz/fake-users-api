from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

from users_api.gen_users import stream_users

app = FastAPI(title="FakeUsers", version="1.0")


@app.get("/users")
def users(page: int = Query(1, ge=1), size: int = Query(20, ge=1, le=100)):
    payload = list(stream_users(page=page, size=size))
    return JSONResponse(payload)
