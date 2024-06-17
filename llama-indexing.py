from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API KEY" + api_key[0:6])
else:
    print("API Key not found")

documents = SimpleDirectoryReader("pdf").load_data()
index = VectorStoreIndex.from_documents(documents)
engine = index.as_query_engine()

result = engine.query("Why is Honda Accord better than Toyota prius?")

print(result)

index.storage_context.persist("hybrid-cars-index")
