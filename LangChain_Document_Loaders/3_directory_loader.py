from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader=DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()

print(docs[256].page_content)