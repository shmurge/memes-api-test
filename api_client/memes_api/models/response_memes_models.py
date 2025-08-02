from pydantic import BaseModel, Field
from typing import Optional, Union, List, Dict


class ResponseMemeModel(BaseModel):
    id: int
    info: Optional[Dict]
    tags: Optional[List]
    text: str
    updated_by: str
    url: str

class ResponseMemeListModel(BaseModel):
    data: ResponseMemeModel