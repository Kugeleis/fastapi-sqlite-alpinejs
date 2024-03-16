from pyclbr import Class
from typing import List, Optional

from sqlalchemy import table
from sqlmodel import Field, Relationship, SQLModel


class Employee(SQLModel, table=True):
    id: int = Field(primary_key=True)
    first_name: str
    surname: str
    job_title: str
    department_id: Optional[int] = Field(None, foreign_key="department.id")
    department: Optional["Department"] = Relationship(back_populates="employee")


class Department(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    employees: List["Employee"] = Relationship(back_populates="department")
