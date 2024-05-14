"""
api.py

© 2024, Bob Lee
"""

import os
import sys
import json
import time
import logging
from uuid import uuid4

from dotenv import dotenv_values
from fastapi import FastAPI, Request, HTTPException, status, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

sys.path.append(os.path.join(os.getcwd(), "packages"))
from Models import Object

app = FastAPI()
env = dotenv_values(".env."+os.environ["NODE_ENV"])
router = APIRouter(prefix=env["BASE_PATH"])
host = env["JOB_HOST"]
port = int(env["JOB_PORT"])

SERVICE_URL = env["PROTOCOL"] + env["SERVICE_URL"] + ":" + env["SERVICE_PORT"]

origins = ["*"]
app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"]
        )

@router.get("/")
def root():
    """ Returns health
    """
    return "api"

app.include_router(router)

if __name__=="__main__":
    uvicorn.run("api:app",host=env["SELF_INTERFACE"], port = port, log_level="info", reload=True)
    logging.info("Running on http://%s:%s" % (host, str(port)))
