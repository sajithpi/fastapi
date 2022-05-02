from ast import For
from fastapi import FastAPI,Form,Depends
from fastapi.params import Body
from pydantic import BaseModel
from model import User,Account,Profile,Session,engine,desc
from schemas import Post
app = FastAPI()




    

@app.get("/")
def read_root():
    return {"message","hello world"}


            
@app.post("/createposts")
async def create_posts(new_post: Post = Depends(Post.as_form)):
    print("username:",new_post.title)
    print("new post:",new_post)
    return {'message':'successfully created posts'}

@app.post("/createuser")
async def create_user(username:str = Form(...),email:str = Form(...),sponser_id:int = Form(...),adrs:str=Form(...)):
    local_session = Session(bind=engine)
    print("username:",username)
    print("email:",email)
    print("Sponser id:",sponser_id)
    print("address:",adrs)

    try:
        add_user = User(username=username, email=email)
        local_session.add(add_user)
      

        new_id = local_session.query(User).order_by(desc(User.id)).first()
        print("new id:",new_id.id)
        add_profile = Profile(user_id=new_id.id,sponser_id = sponser_id,address = adrs)
        local_session.add(add_profile)
        local_session.commit()
        return {'message':'successfully created users'}
    except:
        return {'message':'not created'}
    
