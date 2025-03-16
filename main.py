#Importar bibliotecas
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

#Estrutura dos dados
class Task(BaseModel):
    id: int
    title: str
    column: str

#Banco de Dados temporário
tasks = [
    Task(id=1, title= "Tarefa 1", column="todo"),
    Task(id=2, title= "Tarefa 2", column="inprogress"),
    Task(id=3, title= "Tarefa 3", column="done"),
]

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"message": "Tarefa adicionada com sucesso!"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, column: str):
    for task in tasks:
        if task.id == task_id:
            task.column = column
            return {"message": "Tarefa atualizada!"}
    return {"error": "Tarefa não encontrada!"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Tarefa removida!"}
