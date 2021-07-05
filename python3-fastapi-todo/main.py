from fastapi import FastAPI, HTTPException
from typing import Optional, List
from model import Todo
from database import (create_todo, fetch_all_todos, update_todo, fetch_one_todo, remove_todo)
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [ 'http://localhost:3000', ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        )

@app.get('/api/v1/todo')
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.post('/api/v1/todo', response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong')


@app.put('/api/v1/todo/{title}', response_model=Todo)
async def put_todo(title: str, description: str, done: bool):
    response = await update_todo(title, description, done)
    if response:
        return response
    raise HTTPException(404, f'There is no todo with the title {title}')



@app.get('/api/v1/todo/{title}', response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f'There is no todo with the title {title}')


@app.delete('/api/v1/todo/{title}')
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return 'Successfully deleted todo'
    raise HTTPException(404, f'There is no todo with the title {title}')
