import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

def main():
  load_dotenv()

  if os.getenv("OPEN_API_KEY") is None or os.getenv("OPEN_API_KEY") == "":
    print("OPEN_API_KEY is not set")
    exit(1)
  else:
    print('OPEN_API_KEY is set')


  st.set_page_config(
    page_title = "Personal Chatbot",
    page_icon = "💬"
  )

  st.header("Welcome to your Chatbot 🤖")

 

  with st.sidebar:
    user_input = st.text_input("Your message: ", key = "user_input")

  message("Hello, how are you?")
  message("Hi, I am fine", is_user = True)
  


if __name__ == "__main__":
  main()
