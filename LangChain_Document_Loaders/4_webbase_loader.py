from langchain_community.document_loaders import WebBaseLoader
import os

os.environ["USER_AGENT"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

url='https://www.linkedin.com/feed/'

loader=WebBaseLoader(url)

docs=loader.load()

print(docs[0].page_content)