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

@app.get("/delete_user")  # Изменено с @app.delete на @app.get
async def delete_users(request: Request):
    return templates.TemplateResponse("delete.html", {
        "request": request,
        "users": users  # Передаем список пользователей для удаления
    })

@app.post("/delete")
async def delete_user(
    id_user: int = Form(...)  # Используем Form
):
    delete(id_user)
    return {"message": "пользователь удалён"}

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {
        "request": request
    })

@app.get("/log")
async def log(
    request: Request,
    name: str,  # Эти параметры будут из query string
    age: int
):
    user = searches(name=name, age=age)
    if user:
        return templates.TemplateResponse("glava.html", {
            "request": request,
            "user": user  # Передаем пользователя в шаблон
        })
    else:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error": "Пользователь не найден"
        })