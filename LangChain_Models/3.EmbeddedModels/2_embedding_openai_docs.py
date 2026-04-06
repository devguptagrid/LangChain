from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimenstions=32)

documents=[
    "Delhi is the capital of india",
    "Bangalore is the capital of Karnataka",
    "Mumbai is the capital of Maharashtra"
]
result=embedding.embed_documents(documents)

print(str(result))  