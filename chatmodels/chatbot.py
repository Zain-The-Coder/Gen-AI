from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage , SystemMessage

model = ChatMistralAI(model="mistral-small-2506", temperature=0.1, max_tokens=200)

print("Press 1 for angry mode")
print("Press 2 for sad mode")
print("Press 3 for funny mode")

choice = int(input("Enter the number to setup your mode"))

if choice == 1 :
    mode = "You are angry AI , talk me with angry behaviour"
elif choice == 2 : 
    mode = "You are sad AI , talk me with sad behaviour"
elif choice == 3 :
    mode = "You are funny AI , talk me with funny behaviour"
else : 
    print("Please select anyone from the above number")
messages = [
    SystemMessage(content=mode)
]

print("________Type 0 to exit the application_________")
while True:
    prompt = input("You : ")
    if prompt == "0":
        break

    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot : ", response.content)