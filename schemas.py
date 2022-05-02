from fastapi import Form
from pydantic import BaseModel
class Post(BaseModel):
    title:str
    description:str
    
    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        description: str = Form(...)
    ):
        return cls(
            title=title,
            description=description
        )
