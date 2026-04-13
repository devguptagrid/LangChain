from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableBranch, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
 template='Summarize the following text {text}',
 input_variables=['text']
)

report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>200, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

print(final_chain.invoke({'topic':'cricket'}))