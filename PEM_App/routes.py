from typing import List

from fastapi import Depends, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from typing_extensions import Annotated

from sqlalchemy.orm import Session

from PEM_App import app, schemas, crud, get_db # oauth2_scheme

templates = Jinja2Templates(directory="./PEM_App/templates")

@app.get("/")
async def hello_world(request: Request):
    return templates.TemplateResponse("hello_world.html", {"request": request})


@app.post("/", response_model=schemas.ItemBase)
async def get_input_context(item: schemas.ItemBase, request: Request):
    print('Printing')
    print(item)

    context = {
        "title" : item.title,
        "description" : item.description,
        "context" : item.title + " " + item.description
    }

    print (context)
    
    return JSONResponse(content=context)
    # return templates.TemplateResponse("print_input.html", context=context)

# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items


