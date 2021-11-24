from schematics.models import Model
from schematics.types import StringType, ListType, IntType
from pydantic import BaseModel
from bson import ObjectId

class User(Model):
    user_id = ObjectId()
    username = StringType(required=True)
    password = StringType(required=True)
    money = IntType(required=True)
    plates = ListType(StringType)

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str