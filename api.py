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
from Models.Object import Obj
from Apps.sub_app import sub_app

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)


@asynccontextmanager
async def lifespan(app : FastAPI):
    logger.debug("Running on http://%s:%s" % (host, str(port)))
    persist_obj = {"obj": "This is my stateful object that can be referenced across all routes & sub-apps"}
    yield {"persist_obj": persist_obj}
    persist_obj.clear()
    return

env = os.environ
TITLE = "Sample API"
APP_DESC =f"""## Sub Apps:
- [{env["BASE_PATH"]}]({env["BASE_PATH"]}/docs): Main API docs
- [{env["SUB_PATH"]}]({env["SUB_PATH"]}/docs): Sub API docs
"""
app = FastAPI(title=TITLE, description=APP_DESC, lifespan=lifespan)
subapp = FastAPI()

host = env["API_HOST"]
port = int(env["API_PORT"])
main_app = FastAPI(root_path = env["BASE_PATH"])

origins = ["*"]
app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"]
        )

@main_app.get("/")
def root(request: Request):
    """ Returns health of the server.
    """
    return request.state.persist_obj

@main_app.post("/api/v1/test")
def test(obj : Obj):
    """ Converts given object into a string.
    """
    obj_dict = jsonable_encoder(obj)
    return json.dumps(obj_dict)

app.mount(env["SUB_PATH"], sub_app)
app.mount(env["BASE_PATH"], main_app)

if __name__=="__main__":
    uvicorn.run("api:app",host=host, port = port, log_level="info", reload=True)
    logging.info("Running on http://%s:%s" % (host, str(port)))
