from fastapi import APIRouter
from typing import List, Optional
import db as connection
from schemas import userModel

router = APIRouter()

# funtion to create and assign values to the instanse of class User created
def create_user(username, password):
    newuser = userModel.User()
    newuser.user_id = userModel.ObjectId()
    newuser.username = username
    newuser.password = password
    newuser.money = 0
    newuser.plates = []
    return dict(newuser)

def username_exists(username):
    user_exist = True
    if connection.db.users.find(
        {'username': username}
    ).count() == 0:
        user_exist = False
        return user_exist

def check_login_creds(username):
    if not username_exists(username):
        activeuser = connection.db.users.find(
            {'username': username}
        )
        for actuser in activeuser:
            actuser = dict(actuser)
            actuser['_id'] = str(actuser['_id'])    
            return actuser

# Signup endpoint with the POST method
@router.post("/signup")
async def signup(user: userModel.UserCreate):
    newuser = user.dict()
    user_exists = False
    data = create_user(newuser['username'], newuser['password'])

    # Checks if an email exists from the collection of users
    if connection.db.users.find(
        {'username': data['username']}
        ).count() > 0:
        user_exists = True
        print("USer Exists")
        return {"message":"User Exists"}
    # If the email doesn't exist, create the user
    elif user_exists == False:
        connection.db.users.insert_one(data)
        return {"message":"User Created","username": data['username'], "pass": data['password']}

# Login endpoint
@router.post("/login")
async def login(user: userModel.UserLogin):
    usernow = user.dict()
    def log_user_in(creds):
        if creds['username'] == usernow['username'] and creds['password'] == usernow['password']:
            return {"message": creds['username'] + ' successfully logged in'}
        else:
            return {"error":"Invalid Password"}
    # Read email from database to validate if user exists and checks if password matches
    logger = check_login_creds(usernow['username'])
    if bool(logger) != True:
        if logger == None:
            logger = "Invalid Username"
            return {"error":logger}
    else:
        status = log_user_in(logger)
        return status
