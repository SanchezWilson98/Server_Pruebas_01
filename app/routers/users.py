from typing import Union
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
        id: int;
        name: str;
        surname: str;
        url: str;
        age: int;

class Item(BaseModel):
    ESP_1: Union[User, None] = None

users_list = [Item(ESP_1= User(id=1,name="wilson",surname= "dev", url="http://hello", age=31)),
         Item(ESP_1=User(id=2, name="Andres", surname="dev2", url="http://hello2", age=5)),
         Item(ESP_1=User(id=3,name="wilson2", surname="dev3", url="http://hello3", age=20))]

@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}


@router.post("/user/",status_code=201) #codigo si todo sale bien S
async def user(user: Item):
    """if type(search_user(user.ESP_1.id)) == User:
        raise HTTPException(status_code=204, detail="El susuario ya existe") #Lanzar Error raise 
        #return {"Error": "El Usuario ya existe"}

    else:
        users_list.append(user)"""
    users_list.append(user)
    return user




def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}