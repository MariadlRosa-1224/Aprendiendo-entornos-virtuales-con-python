from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse

app = FastAPI() # Create a FastAPI instance


@app.get("/items/")
async def read_items():
    return FileResponse("html/index.html")


@app.get("/") # Decorator
def get_list(): # this function is the path operation function
    return [1,2,3] # this is the response body

@app.get('/contact')
def get_list():
    return {"name": 'Maria: email'}

