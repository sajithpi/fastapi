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
class Users(BaseModel):
    username:str
    email:str
    sponser_id:int
    adrs : str
    
    @classmethod
    def as_form(
        cls,
        username:str = Form(...),
        email:str = Form(...),
        sponser_id:int = Form(...),
        adrs : str = Form(...)
    ):
        return cls(
            username=username,email=email,sponser_id=sponser_id,adrs=adrs
        )
