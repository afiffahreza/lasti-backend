from fastapi import FastAPI
from routes import userAuth, userPlate, userMoney
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(userAuth.router, tags=["Auth"])
app.include_router(userPlate.router, tags=["Plate"])
app.include_router(userMoney.router, tags=["Money"])

# Our root endpoint
@app.get("/")
def root():
    return {"message": "Hello World"}
