from starlette.templating import Jinja2Templates
from db import users
from fastapi import FastAPI, Request, Form  # Добавлен Form
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
    })

@app.get("/create_user")
async def create_users(request: Request):
    return templates.TemplateResponse(
        "create.html", {
            "request": request
    })

@app.post("/create")
async def create_user(
    request: Request,
    name: str = Form(...),
    age: int = Form(...)
):
    create(name=name, age=age)
    return templates.TemplateResponse(
        "create.html", {
            "request": request,
            "message": f"Пользователь {name} успешно создан!"
    })

@app.get("/delete_user")
async def delete_users(request: Request):
    return templates.TemplateResponse("delete.html", {
        "request": request,
        "users": users
    })

@app.post("/delete")
async def delete_user(
    id_user: int = Form(...)
):
    delete(id_user)
    return {"message": "пользователь удалён"}

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {
        "request": request
    })

@app.get("/logins")
async def logins(request: Request):
    return templates.TemplateResponse("logins.html", {
        "request": request
    })

@app.get("/log")
async def log(
    request: Request,
    name: str,
    age: int
):
    user = searches(name=name, age=age)
    if user:
        return templates.TemplateResponse("glava.html", {
            "request": request,
            "user": user
        })
    else:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error": "Пользователь не найден"
        })


@app.get("/logs")
async def logs(
    request: Request,
    name: str,
    age: int
):
    user = searches(name=name, age=age)
    if user:
        return templates.TemplateResponse("glava.html", {
            "request": request,
            "user": user
        })
    else:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error": "Пользователь не найден"
        })