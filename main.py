from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import uvicorn
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API KEY" + api_key[0:6])
else:
    print("API Key not found")
app = FastAPI()

storage_context = StorageContext.from_defaults(persist_dir="ml_index")
index = load_index_from_storage(storage_context)
engine = index.as_query_engine()

class Item(BaseModel):
    number1: float
    number2: float

class Query(BaseModel):
    question: str

@app.get("/")
async def read_root():
    return {"message": "Hello World!"}


@app.post("/sum")
async def sum(item: Item):
    return("result: " +  item.number1 + item.number2)


@app.post("/query")
async def query(query: Query):
    result = engine.query(query.question)
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port = 8090, reload = True)
