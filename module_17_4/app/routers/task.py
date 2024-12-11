from fastapi import APIRouter


router = APIRouter(prefix="/task", tags=["task"])


# Главная
@router.get("/")
async def all_task():
    pass


# Информация
@router.get("/task_id")
async def task_by_id():
    pass


# Добавление
@router.post("/create")
async def create_task():
    pass


# Изменение
@router.put("/update")
async def update_task():
    pass


# Удаление
@router.delete("/delete")
async def delete_task():
    pass
