from ast import For
from fastapi import FastAPI,Form,Depends
from fastapi.params import Body
from pydantic import BaseModel
from model import User,Account,Profile,Session,engine,desc
from schemas import Post,Users
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
async def create_user(new_user:Users = Depends(Users.as_form)):
    local_session = Session(bind=engine)
    print("username:",new_user.username)
    print("email:",new_user.email)
    print("Sponser id:",new_user.sponser_id)
    print("address:",new_user.adrs)

    try:
        # add_user = User(username=new_user.username, email=new_user.email)
        # local_session.add(add_user)
      

        new_id = local_session.query(User).order_by(desc(User.id)).first()
        print("new id:",new_id.id)
        # add_profile = Profile(user_id=new_id.id,sponser_id = new_user.sponser_id,address = new_user.adrs)
        # local_session.add(add_profile)
        # local_session.commit()
        return {'message':'successfully created users'}
    except:
        return {'message':'not created'}
    
