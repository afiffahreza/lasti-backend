from bson.objectid import ObjectId
from fastapi import APIRouter
import db as connection
from schemas import tollModel
from bson import ObjectId, json_util
import json

router = APIRouter()

def create_toll_data(id, name, price):
    toll = tollModel.Toll()
    toll.t_id = ObjectId()
    toll.toll_id = id
    toll.name = name
    toll.price = price
    return dict(toll)

@router.get("/tolls")
async def get_tolls():
    data = connection.db.tolls.find({},{'_id': 0})
    return json.loads(json_util.dumps(data))

@router.get("/toll/{toll_id}")
async def get_tolls_by_id(toll_id: str):
    query = {"toll_id": toll_id}
    data = connection.db.tolls.find_one(query,{'_id': 0})
    return json.loads(json_util.dumps(data))

@router.post("/toll")
async def create_toll(newtoll: tollModel.TollCRUD):
    toll = newtoll.dict()
    data = create_toll_data(toll['toll_id'], toll['name'], toll['price'])
    if connection.db.tolls.find({'toll_id': data['toll_id']}).count() > 0:
        return {"message":"Toll already exists"}
    else:
        connection.db.tolls.insert_one(data)
        return {"message":"Toll Created","Toll ID": data['toll_id'], "Toll name": data['name'], "Toll price":data['price']}

@router.delete("/toll/{toll_id}")
async def delete_toll(toll_id: str):
    if connection.db.tolls.find({'toll_id': toll_id}).count() == 0:
        return {"message":"Toll doesn't exists"}
    else:
        data = connection.db.tolls.find_one_and_delete({'toll_id': toll_id},{'_id': 0})
        data = json.loads(json_util.dumps(data))
        return {"message":"Toll successfully deleted", "data":data}