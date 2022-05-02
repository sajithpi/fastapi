from model import User,Post,Session,engine,exc
class Posts:
    def __init__(self):
        
        self.local_session = Session(bind=engine)
        self.count=1
    def show_post_by_user(self):
        # for u, p in local_session.query(User,Post).filter(User.id == 3).all():
        #     print(u.id,u.username,p.post_name)
        if(self.local_session.query(Post).count()==self.count):
            return 1
        else:
            self.result = self.local_session.query(Post).filter(Post.id==self.count).first()
            self.count += 1 
            # print(self.result[0])     
            if self.result:
                print("True",self.count)
               
            else:
                print("False") 
            return ob1.show_post_by_user()

                
ob1 = Posts()
ob1.show_post_by_user()