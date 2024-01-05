from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None

db = DataBase()

async def get_database() -> AsyncIOMotorClient:
    return db.client

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(str()) ## get frmo compose

async def close_mongo_connection():
    db.client.close()
    