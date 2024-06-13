"""
api.py

"""
__author__ = "Your Name"

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
env = os.environ
router = APIRouter(prefix=env["BASE_PATH"])
host = env["API_HOST"]
port = int(env["API_PORT"])

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
    uvicorn.run("api:app",host=host, port = port, log_level="info", reload=True)
    logging.info("Running on http://%s:%s" % (host, str(port)))
