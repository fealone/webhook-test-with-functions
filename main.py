from typing import Any, Dict

from agraffe import Agraffe

from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/printf")
async def printf(request: Request) -> Dict[str, str]:
    body = await request.json()
    print(body)
    return {}


def entry_point(request: Any) -> Agraffe:
    agraffe = Agraffe(app)
    return agraffe(request)
