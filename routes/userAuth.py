from fastapi import APIRouter
from typing import List, Optional
import db as connection
from schemas import userModel

router = APIRouter()

# funtion to create and assign values to the instanse of class User created
def create_user(email, username, password):
    newuser = userModel.User()
    newuser.user_id = userModel.ObjectId()
    newuser.email = email
    newuser.name = username
    newuser.password = password
    newuser.money = 0
    newuser.plates = ["B44HA"]
    return dict(newuser)

def email_exists(email):
    user_exist = True
    if connection.db.users.find(
        {'email': email}
    ).count() == 0:
        user_exist = False
        return user_exist

def check_login_creds(email, password):
    if not email_exists(email):
        activeuser = connection.db.users.find(
            {'email': email}
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
    data = create_user(newuser['email'], newuser['name'], newuser['password'])

    # Checks if an email exists from the collection of users
    if connection.db.users.find(
        {'email': data['email']}
        ).count() > 0:
        user_exists = True
        print("USer Exists")
        return {"message":"User Exists"}
    # If the email doesn't exist, create the user
    elif user_exists == False:
        connection.db.users.insert_one(data)
        return {"message":"User Created","email": data['email'], "name": data['name'], "pass": data['password']}

# Login endpoint
@router.post("/login")
async def login(user: userModel.UserLogin):
    usernow = user.dict()
    def log_user_in(creds):
        if creds['email'] == usernow['email'] and creds['password'] == usernow['password']:
            return {"message": creds['name'] + ' successfully logged in'}
        else:
            return {"message":"Invalid credentials!!"}
    # Read email from database to validate if user exists and checks if password matches
    logger = check_login_creds(usernow['email'], usernow['password'])
    if bool(logger) != True:
        if logger == None:
            logger = "Invalid Email/Password"
            return {"message":logger}
    else:
        status = log_user_in(logger)
        return {"Info":status}
