from typing import List
from fastapi import APIRouter
import db as connection
from pydantic import BaseModel

router = APIRouter()

class Plate(BaseModel):
    plates: List[str]

@router.put("/plates/{username}")
async def update_plate(username: str, add_plate: Plate):
    query = {'username': username}
    if connection.db.users.find(query).count() == 0:
        return {"error":"No username found"}
    else:
        np = add_plate.dict()
        newval = { "$set": { "plates": np['plates'] } }
        connection.db.users.update_one(query, newval)
        return newval