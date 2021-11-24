from typing import List
from fastapi import APIRouter
import db as connection
from pydantic import BaseModel

router = APIRouter()

class Money(BaseModel):
    money: int

@router.put("/money/{username}")
async def update_money(username: str, add_money: Money):
    query = {'username': username}
    if connection.db.users.find(query).count() == 0:
        return {"error":"No username found"}
    else:
        nm = add_money.dict()
        newval = { "$set": { "money": nm['money'] } }
        connection.db.users.update_one(query, newval)
        return newval