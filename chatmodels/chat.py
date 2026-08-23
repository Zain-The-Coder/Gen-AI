from dotenv import load_dotenv
load_dotenv()

# from langchain_google_genai import ChatGoogleGenerativeAI

# model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")

# response = model.invoke("What Is LLM ?")
# print(response.content)

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506" , temperature=0.1 , max_tokens=20)
response = model.invoke("What Is Best Football player , name only one")

print(response.content)