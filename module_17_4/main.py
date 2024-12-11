from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()
info_ed = ('<h2>Домашнее задание по теме "Использование БД в маршрутизации. 1.1"<br>'
           '<h3>Цель: научиться управлять записями в БД используя SQLAlchemy и маршрутизацию FastAPI.'
           '<br>Задача "Маршрутизация пользователя":'
           '<br>Студент Крылов Эдуард Васильевич'
           '<br>Дата: 11.12.2024г.</h3>')


# python -m uvicorn main:app
# Get
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


@app.get("/info", response_class=HTMLResponse)
async def info():
    return info_ed


app.include_router(task.router)
app.include_router(user.router)
# alembic revision --autogenerate -m "Initial migration"
# python main.py migrate
# python -m uvicorn main:app
# uvicorn main:app --reload
