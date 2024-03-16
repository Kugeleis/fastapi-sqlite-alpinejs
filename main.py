from typing import List

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import Department, Employee

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/employees", response_class=HTMLResponse)
def employees(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("employees.html", context)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
