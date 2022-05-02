
from os import stat
from fastapi import FastAPI,Form,Depends, HTTPException,Response,status
from fastapi.params import Body
from pydantic import BaseModel
from model import User,Account,Profile,Session,engine,desc
from schemas import Post,Users
app = FastAPI()


@app.get("/")
def read_root():
    return {"message","hello world"}


#Function to create posts
    
@app.post("/createposts")
async def create_posts(new_post: Post = Depends(Post.as_form)):
    print("username:",new_post.title)
    print("new post:",new_post)
    return {'message':'successfully created posts'}


# Function To Create Users

@app.post("/createuser",status_code=status.HTTP_201_CREATED)
async def create_user(new_user:Users = Depends(Users.as_form)):
    local_session = Session(bind=engine)
    print("username:",new_user.username)
    print("email:",new_user.email)
    print("Sponser id:",new_user.sponser_id)
    print("address:",new_user.adrs)

    try:
        add_user = User(username=new_user.username, email=new_user.email)
        local_session.add(add_user)
      

        new_id = local_session.query(User).order_by(desc(User.id)).first()
        print("new id:",new_id.id)
        add_profile = Profile(user_id=new_id.id,sponser_id = new_user.sponser_id,address = new_user.adrs)
        local_session.add(add_profile)
        local_session.commit()
        return {'message':'successfully created users'}
    except:
        return {'message':'not created'}
    
 
#Retrieving user details 
 
@app.get("/users/{id}")
def get_user(id:int,response:Response):
    print(type(id))
    local_session = Session(bind=engine)
    user = local_session.query(User).filter(User.id==id).first()
    if user:
        print(user.id)
        return {'message':'success',
                'id':user.id,
                'name':user.username
                }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")

#Delete User Details
 
@app.delete("/deleteuser/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int):
    local_session = Session(bind=engine)
    user = local_session.query(User).filter(User.id==id).first()
    if user:
        local_session.delete(user)
        local_session.commit()
        
        return {'message':'deleted'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} doesn't exist")
   
# Updating user details

@app.put("/updateuser/{id}")
def update_user(id:int,update_user:Users = Depends(Users.as_form)):
    print(id)
    
    local_session = Session(bind=engine)
    profile = local_session.query(Profile).filter(Profile.user_id==id).first()
    if profile:
        profile.address = update_user.adrs
        local_session.commit()
        return {'message':'updated user successfully',
                'address':update_user.adrs}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} doesn't exist")
