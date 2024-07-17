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
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, HTTPException, status, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

import uvicorn

sys.path.append(os.path.join(os.getcwd(), "packages"))
from Models import Object

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

persist_obj = {}

@asynccontextmanager
async def lifespan(app : FastAPI):
    logger.debug("Running on http://%s:%s" % (host, str(port)))
    persist_obj['current'] = """
            This is my global, persistent object,
            that can be referenced across all routes.
            """
    yield
    persist_obj.clear()
    return

app = FastAPI(lifespan=lifespan)
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
    """ Returns health of the server.
    """
    return persist_obj["current"]

@router.get("/api/v1/test")
def test(obj : Object):
    """ Converts given object into a string.
    """
    obj_dict = jsonable_encoder(obj)
    return json.dumps(obj_dict)

app.include_router(router)

if __name__=="__main__":
    uvicorn.run("api:app",host=host, port = port, log_level="info", reload=True)
    logging.info("Running on http://%s:%s" % (host, str(port)))
