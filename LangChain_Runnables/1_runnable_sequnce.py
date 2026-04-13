from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Explain the following {joke}',
    input_variables=['joke']
)


chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':'cricket'}))