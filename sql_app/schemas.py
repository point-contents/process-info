from typing import List, Union

from pydantic import BaseModel

class ExtendedBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Process(ExtendedBaseModel):
    id: str
    name: str
    host: str
    source: str
    destination: str

class ProcessOut(ExtendedBaseModel):
    id: str
    name: str
    host: str | None = None
    source: str | None = None
    destination: str | None = None

class FoundProcess(ExtendedBaseModel):
    id: str

class HostOut(ExtendedBaseModel):
    id: str
    name: str
    source: str | None
    destination: str | None


