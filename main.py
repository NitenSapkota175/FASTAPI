from importlib.resources import contents
from turtle import title
from fastapi import  FastAPI #importing fastapi
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
app = FastAPI() #creating an instance of fastapi app can whaterve you want to name it but it better we follow up the convention FASTAPI() is fucntion so to create an insntace we are calling the function

class Post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating :Optional[int] = None #this going to be fully optional field if user doesn;t provides it is going to be none  

@app.get("/") #this is decorate if you remove this it justa plan function and not api ,this dectorate turns this function to path operation so if someone wants to use our api can hit this end point , @app.get app is fastapi instace instace we created  get is http method jsut like in django its is get request andn we have ddiferent http method look it into http method and isnide get() we have to specify the path '/' this is the root path 
#this whole thing is called path operation in other programmin languages it can be refered different like route but in fastapi documentation it is called path operation
async def root(): #this is a function is no different than python that async keyword is optional async means this keyword is only need if you are performig  with the some sort of  asynchronic task some that takes creatian amount of time so things like making an api call things like talking to the database fi you wnt to do that asynchorisly you need that keyword root() the name doesn't matter you can name it whatever you want  
    return {"message": "Hello World"} #just like anyother function we can return something whatever we return here is going to be the data that is sent  back to the user 
    # we are passing here python dictionary and what happens is fastapi will automatically covert this JSON which is the main universal language of api we use json to send data back and forth between api so  




#to satrt our websever app we need how to start our websever ?we will use uvicorn main:app main is main.py file you can name it whatever you want and the instance name here we have created with FASTAPI() in this case it is app
#command : uvicorn main:app this will satrt the webserver 



# NOTE : if change something in the code and save it and go in the browser and reload the user there you can see that nothing change that's because if change anything in the code and inorder for those change to be reflected what we need to is restart the server it is quite annoying to that right there is a other way around when you are restarting the server do --reload like uvicorn main:app --reload tis willa utomatically reload the server 
#fastapi go through the code and looks for firt match lets if you sepcify the path for two path operation then it is going to take the first one sand desktop running the code ,the order actually matters 
@app.get('/post')
def get_post():
    return {"data" : "this is you post"}


#here is post request in get request we are saying that go the specified url and get some data but in post request we can specify the data we want and send that data to an api and retrive that data and store it in the database right now we are settting on the data we are just send the data to user , if the create_post function we are making the payload variable createng the dictionary and getting the data from the body a and storing that data in the python dictionary 

@app.post("/createposts")
def create_posts(post: Post ):
#when we extrack the data and save it in new post it actual sstore as it has pydantic model it is a specific pydantic model each pydantic model hs a model called .dict which convert this pydantic model to dictionary and each pydantic model has method called .dict 
    print(post) #printing pydantic model 
    print(post.dict()) #covertin pydantic model to the dictionary ,regular dictionary 
    return {"data" : post}
