from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from .db.mongodb import connect_to_mongo, close_mongo_connection
from .api.api import router as api_router

app = FastAPI(title="Balak API")

# app.add_middleware(
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

@app.get('/')
async def root():
    return {'message': 'Hello World'}

app.include_router(api_router, prefix='/api')