from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough
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

joke_gen_chain=RunnableSequence(prompt1, model, parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_Chain=RunnableSequence(joke_gen_chain,parallel_chain)

print(final_Chain.invoke({'topic':'cricket'}))