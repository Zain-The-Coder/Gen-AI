from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage

model = ChatMistralAI(model="mistral-small-2506", temperature=0.1, max_tokens=200)
messages = []

print("________Type 0 to exit the application_________")
while True:
    prompt = input("You : ")
    if prompt == "0":
        break

    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot : ", response.content)