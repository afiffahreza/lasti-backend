from schematics.models import Model
from schematics.types import StringType, EmailType, ListType, IntType
from pydantic import BaseModel
from bson import ObjectId

class User(Model):
    user_id = ObjectId()
    email = EmailType(required=True)
    name = StringType(required=True)
    password = StringType(required=True)
    money = IntType(required=True)
    plates = ListType(StringType)

class UserCreate(BaseModel):
    email: str
    name: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str