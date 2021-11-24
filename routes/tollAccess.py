from bson.objectid import ObjectId
from fastapi import APIRouter
import db as connection
from schemas import tollModel
from bson import ObjectId, json_util
import json

router = APIRouter()

@router.get("/access/{toll_id}/{plate}")
async def read_access(toll_id: str, plate: str):
    tollData = connection.db.tolls.find_one({'toll_id': toll_id})
    price = tollData['price']
    userData = connection.db.users.find_one({ 'plates': { '$in': [plate] } })
    if userData:
        print(userData)
        newbal = userData['money'] - price
        newval = { "$set": { "money": newbal } }
        connection.db.users.update_one({'username': userData['username']}, newval)
        return {"message": "Success", "username": userData['username'], "new balance":newbal}
    return {"error": "not found"}