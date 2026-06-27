from fastapi import FastAPI,Request
#from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app=FastAPI()
#Telling FastAPI where to look for templates
templates=Jinja2Templates(directory="templates")
posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]
# @app.get("/") ---returns response as json format
# async def root():
#     return {"msg":"Hello"}

#-------If we want to return in HTML reponse
# @app.get("/",response_class=HTMLResponse)
#@app.get("/",response_class=HTMLResponse,include_in_schema=False) --won't appear in documentation
#@app.get("/posts",response_class=HTMLResponse) -- if we want same functionality for posts as well
@app.get("/",include_in_schema=False)
@app.get("/posts",include_in_schema=False) 
async def root(request:Request):
    return templates.TemplateResponse(request,"home.html",
                                      {"posts":posts,"title":"Home"},
    )

@app.get('/api/posts')
def get_posts():
    return posts