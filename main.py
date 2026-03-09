from starlette.templating import Jinja2Templates
from db import users
from fastapi import FastAPI, Request
from db import create, delete, searches

templates = Jinja2Templates(directory="templates")
app = FastAPI()

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "users": users,
            "Title": "Тестовый сайт"
    }
    )

@app.get("/create_user")
async def create_users(request: Request):
    return templates.TemplateResponse(
        "create.html", {
            "request": request
    })

@app.post("/create")
async def create_user(name: str, age: int):
    create(
        name=name, age=age
    )
    return {"message": "пользователь создан"}

@app.post("/delete")
async def delete_user(id_user: int):
    delete(
        id_user
    )
    return {"message": "пользователь удалён"}

@app.delete("/delete_user")
async def delete_users(request: Request):
    return templates.TemplateResponse("delete.html", {
        "request": request
    })

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {
        "request": request
    })
@app.get("/log")
async def log(request: Request, name: str, age: int):
    user = searches(name=name, age=age)
    if user:
        return templates.TemplateResponse("glava.html", {
            "request": request,
        })
    else:
        return templates.TemplateResponse("error.html", {
            "request": request,
        })