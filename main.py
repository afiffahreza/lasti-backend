from fastapi import FastAPI
from routes import users
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)

# Our root endpoint
@app.get("/")
def index():
    return {"message": "Hello World"}
