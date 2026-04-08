from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact-1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact-2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact-3',description='Fact 3 about the topic'),
]

parser=StructuredOutputParser.from_response_schema(schema)

template=PromptTemplate(
    template='Give 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

##without chain
# prompt=template.invoke({'topic':'black hole'})

# result=model.invoke(prompt)

# final_result=parser.parse(result.content)

chain=template | model | parser
final_result=chain.invoke({'topic':'black hole'})
print(final_result)
