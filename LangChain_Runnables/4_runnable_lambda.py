from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

def word_count(text):
    return len(text.split())

prompt1=PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt1, model, parser)

parallel_chain=({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic':'cricket'}))