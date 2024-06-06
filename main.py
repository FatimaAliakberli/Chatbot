import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
  SystemMessage, 
  HumanMessage, 
  AIMessage
)

def init():
  load_dotenv()

  if os.getenv("OPEN_API_KEY") is None or os.getenv("OPEN_API_KEY") == "":
    print("OPEN_API_KEY is not set")
    exit(1)
  else:
    print('OPEN_API_KEY is set')



def main():
  init()

  chat = ChatOpenAI(temprature = 0)

  messages = [
    SystemMessage(content = "You are a helpful assistant.")
  ]


  st.set_page_config(
    page_title = "Personal Chatbot",
    page_icon = "💬"
  )

  st.header("Welcome to your Chatbot 🤖")

 

  with st.sidebar:
    user_input = st.text_input("Your message: ", key = "user_input")

  if user_input:
    message(user_input, is_user = True)
    messages.append(HumanMessage(content = user_input))
    response = chat(messages)
    message(user_input, is_user = False)
  


if __name__ == "__main__":
  main()
