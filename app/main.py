import json
from typing import List
from unittest import result

import uvicorn
from fastapi import Depends, FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from database import get_session
from models import Department, Employee

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/employees", response_class=HTMLResponse)
def employees(request: Request, session: Session = Depends(get_session)):
    # employees = session.exec(select(Employee))
    stmt = select(Employee, Department).where(Employee.department_id == Department.id)
    result = session.exec(stmt).all()
    employee_data = jsonable_encoder(result)
    departments = set([emp["Department"]["name"] for emp in employee_data])
    print("emp: ", employee_data[0])
    context = {
        "request": request,
        "employees": json.dumps(employee_data),
        "departments": departments,
    }
    return templates.TemplateResponse("employees.html", context)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
