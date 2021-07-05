from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    descrption: str
    done: bool
