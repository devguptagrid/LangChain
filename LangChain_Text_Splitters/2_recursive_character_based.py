from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


text="""
Permissions Management: You cannot use IAM policies to deny access to the root user. In contrast, IAM users follow the principle of least privilege, meaning they have zero permissions by default and must be explicitly granted what they need.
Security Risk: Because it has absolute power, the root user is a high-security risk. If compromised, an attacker can delete everything or close the account.
Quantity: Every AWS account has exactly one root user. You can create thousands of IAM users within that single account for different people or applications.
Tasks Only Root Can Do: Only the root user can perform certain critical actions, such as:
Closing the entire AWS account.
Changing account settings (root email, account name, support plan).
Updating payment methods and credit card details.
Enabling IAM access to billing information (initially). 
"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,

)

result=splitter.split_text(text)

print(result)