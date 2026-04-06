from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# text="delhi is the capital of india"
# vector=embedding.embed_query(text)
# print(str(vector))


documents=[
    "Delhi is the capital of india",
    "Bangalore is the capital of Karnataka",
    "Mumbai is the capital of Maharashtra"
]
doc_vector=embedding.embed_documents(documents)
print(str(doc_vector))

