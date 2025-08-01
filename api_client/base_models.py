from pydantic import BaseModel, Field
from typing import Optional, Union, List, Dict


class RequestAuthorizationModel(BaseModel):
    name: Union[str, int, float, List, Dict]


class ResponseAuthorizationModel(BaseModel):
    token: str
    user: str
