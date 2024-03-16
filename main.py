from typing import List

import uvicorn
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from database import get_session
from models import Department, Employee

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/employees", response_class=HTMLResponse)
def employees(request: Request, session: Session = Depends(get_session)):
    employees = session.exec(select(Employee))
    context = {"request": request, "employees": employees}
    return templates.TemplateResponse("employees.html", context)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
