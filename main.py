import os
from typing import Dict

from agraffe import Agraffe, Service

from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/printf")
async def printf(request: Request) -> Dict[str, str]:
    body = await request.json()
    print(body)
    return {}


platform = os.environ.get("PLATFORM", "GCP")

if platform == "GCP":
    entry_point = Agraffe.entry_point(app, Service.google_cloud_functions)
elif platform == "AWS":
    entry_point = Agraffe.entry_point(app, Service.aws_lambda)
else:
    Exception(f"Unsupported platform of {platform}")
