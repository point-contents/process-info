from typing import List, Union

from pydantic import BaseModel

class Process(BaseModel):
    id: str
    name: str
    host: str
    source: str
    destination: str

class ProcessOut(BaseModel):
    id: str
    name: str
    host: str | None = None
    source: str | None = None
    destination: str | None = None 

    class Config:
        orm_mode = True

