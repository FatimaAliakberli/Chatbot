import streamlit as st
from streamlit_chat import message

def main():
  st.set_page_config(
    page_title = "Personal Chatbot",
    page_icon = "💬"
  )

  st.header("Welcome to your Chatbot 🤖")

 

  with st.sidebar:
    user_input = st.text_input("Your message: ", key = "user_input")

  message("Hello, how are you?")
  message("Hi, I am fine", is_user = False)
  


if __name__ == "__main__":
  main()
