from langchain_openai import OpenAI
from dotenv import load_dotenv

## not working as of now as we dont have api key for this model

load_dotenv()

llm=OpenAI(model='gpt-3.5-turbo-instruct')

result=llm.invoke("What is the capital of India?")

print(result)