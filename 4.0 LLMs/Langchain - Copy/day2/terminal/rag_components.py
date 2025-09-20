# from langchain_community.document_loaders import PyPDFLoader, TextLoader
# from pprint import pprint

# loader = PyPDFLoader('./data/ai.pdf')
# # text_loader = TextLoader('./data/ai.txt')

# final_load = loader.load()
# # print(final_load)
# # LOADING THE FIRST DOCUMENT
# print(f"My first document is: {final_load}")

from config import load_embeddings
embeddings=load_embeddings()
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma, FAISS
# Step 1 : Load the document
loader = PyPDFLoader('./data/cameroon_history.pdf')
final_load =loader.load()

print(f"My first document is: {final_load[0].page_content}")

# Step 2 : SPLIT text
text_splitter = CharacterTextSplitter(
    separator="\n\n", 
    chunk_size=1000, # number of words
    chunk_overlap=200, # conecting the last 200 words from the previous chunk to the next. This to maintain the link
    length_function=len, 
    is_separator_regex=False 

)
#regex means regular expression, meaning it should not consider \n as a regular expression
 ## Split Text
 # Python comprehension syntax
 # When you want to use the create_documents method instaed of split_documents an get read of the metadata

page_contents = [doc.page_content for doc in final_load]

text1 =text_splitter.create_documents(page_contents)
text = text_splitter.split_documents(final_load) #this will keep the metadata of the document

chunk1 = text1[2]
chunk = text[1]


# print(len(chunk.page_content))
print('\n')
# print(len(chunk1.page_content))

# Step 3: Vector Stores


#Embeddings and vector stores
vector_db=Chroma.from_documents(text,embeddings, persist_directory= "./chroma_db")

prompt = 'Who was the first president of Cameroon?'
response = vector_db.similarity_search(prompt)
print(f'Response is: {response}' )