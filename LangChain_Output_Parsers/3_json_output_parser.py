## Using str_output_parser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template=PromptTemplate(
    template='Give me the name, age and city of a fictional persom \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
#Method 1
# prompt=template.format()
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)

#Method 2
chain=template | model | parser
final_result=chain.invoke({})

print(final_result)