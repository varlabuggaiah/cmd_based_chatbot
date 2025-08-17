import google.generativeai as genai
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Gemini API Key is not found, please set it in your .env file")
genai.configure(api_key = api_key)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()
#response = chat.send_message("Hello")
#print("Gemini", response.text)
while(True):
    user_input = input("you: ")
    if user_input.lower()=="exit":
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
    


