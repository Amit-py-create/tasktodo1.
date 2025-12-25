from fastapi import APIRouter
from app.database import tasks_collection
from app.models import Task
from bson import ObjectId

router = APIRouter()   # 👈 MUST

@router.post("/tasks")
def create_task(task: Task):
    tasks_collection.insert_one(task.dict())
    return {"message": "Task created"}

@router.get("/tasks")
def get_tasks():
    tasks = []
    for task in tasks_collection.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)
    return tasks

@router.put("/tasks/{task_id}")
def update_task(task_id: str, task: Task):
    tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": task.dict()}
    )
    return {"message": "Task updated"}

@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return {"message": "Task deleted"}
