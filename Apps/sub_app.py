"""
subapp.py

Sub app to be mounted on main FastAPI app.
"""
import os
import sys

from fastapi import FastAPI, Request, HTTPException, status, Response, APIRouter
from fastapi.encoders import jsonable_encoder

sys.path.append(os.path.join(os.getcwd(), "packages"))
from Models.Object import Obj

env = os.environ
sub_app = FastAPI(root_path=env["SUB_PATH"])

@sub_app.get("/")
def test(request: Request):
    """Returns health of subapp.
    """
    # Returns stateful object from parent app
    return request.state.persist_obj

@sub_app.post("/add")
def add(obj: Object):
    """Adds object
    """
    return obj

