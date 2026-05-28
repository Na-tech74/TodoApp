from datetime import datetime
from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)


class TodoUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


class TodoResponse(BaseModel):
    id: int
    title: str
    done: bool
    created_at: datetime | None = None

    class Config:
        from_attributes = True
