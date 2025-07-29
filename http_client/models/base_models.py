from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class RequestAuthorizationModel(BaseModel):
    name: str


class ResponseAuthorizationModel(BaseModel):
    token: str
    user: str

