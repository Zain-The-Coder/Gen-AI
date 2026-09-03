from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()


prompt = ChatPromptTemplate.from_messages([
    ("system" , 
    """
You Are A Professional Movie Information Extraction Assistant .

Your task :
Extract useful structured information from a movie paragraph and present it in a content

Rules : 
-Do not add explanations 
-Do not add extra commentary 
-Follow the exect format 
-If information is missing then write NULL
-keep summary short (2-3 lines max)
-Do not guess unknown facts

OUTPUT FORMAT :

Movie Title : 
Release Year : 
Genre :
Director :
Main Cast :
Setting/Location :
Plot :
Themes :
Rating :
Notable Features :

Short Summary :
    """),
("human" , 
 """
Extract information from this paragraph :

{paragraph}

 """)
 ])

para = input("Give Your Paragraph : ")

final_prompt = prompt.invoke(
    {"paragraph" : para}
)

model = ChatMistralAI(model = 'mistral-small-2506')
response = model.invoke(final_prompt)

print(response.content)