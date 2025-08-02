from pydantic import BaseModel, Field
from typing import Optional, Union, List, Dict


class RequestCreateMemeModel(BaseModel):
    text: Optional[Union[str, int, float, List, Dict]]
    url: Optional[Union[str, int, float, List, Dict]]
    tags: Optional[Union[str, int, float, List, Dict]]
    info: Optional[Union[str, int, float, List, Dict]]


class RequestUpdateMemeModel(BaseModel):
    id: Optional[Union[str, int, float, List, Dict]]
    text: Optional[Union[str, int, float, List, Dict]]
    url: Optional[Union[str, int, float, List, Dict]]
    tags: Optional[Union[str, int, float, List, Dict]]
    info: Optional[Union[str, int, float, List, Dict]]
