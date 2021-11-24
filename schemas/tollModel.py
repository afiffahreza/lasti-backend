from schematics.models import Model
from schematics.types import StringType, IntType
from pydantic import BaseModel
from bson import ObjectId

class Toll(Model):
    t_id = ObjectId()
    toll_id = StringType(required=True)
    name = StringType(required=True)
    price = IntType(required=True)

class TollCRUD(BaseModel):
    toll_id: str
    name: str
    price: int
