from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from typing import Annotated
from pydantic import BaseModel

from PEM_App import crud, models
from PEM_App.database import engine, SessionLocal

# from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

# Create FastAPI applicatopn

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

from PEM_App.routes import *

