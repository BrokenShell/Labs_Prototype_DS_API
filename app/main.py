from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Database
from app.encryption import FernetCypher
from app.machine import Model


API = FastAPI(
    title="Labs Prototype DS API",
    version="0.0.1",
    docs_url="/",
)
API.data = Database()
API.model = Model()
API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.get("/version")
async def api_version():
    return {"API Version": API.version}


@API.get("/secret")
async def labs_secret():
    cypher = FernetCypher()
    return {"Labs Secret": cypher.decrypt(cypher.secret())}


@API.put("/record")
async def create_record():
    return {}


@API.get("/record")
async def read_record():
    return {}


@API.patch("/record")
async def update_record():
    return {}


@API.delete("/record")
async def delete_record():
    return {}
