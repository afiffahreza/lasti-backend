from bson.objectid import ObjectId
from fastapi import APIRouter
import db as connection
from bson import ObjectId, json_util
import json

router = APIRouter()

@router.get("/user/{username}")
async def get_user_by_username(username: str):
    data = connection.db.users.find_one({'username': username},{'_id': 0})
    return json.loads(json_util.dumps(data))
