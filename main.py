from fastapi import FastAPI
from routes import tollService, userAuth, userPlate, userMoney, userService, tollAccess
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
app.include_router(tollService.router, tags=["Tolls"])
app.include_router(userService.router, tags=["User"])
app.include_router(tollAccess.router, tags=["Toll Access"])

# Our root endpoint
@app.get("/")
def root():
    return {"message": "Hello World"}
