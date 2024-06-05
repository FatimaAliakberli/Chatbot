import streamlit as st
#from streamlit_chat import message

def main():
  st.set_page_config(
    page_title = "Personal Chatbot",
    page_icon = "💬"
  )

  st.header("Welcome to your Personal Chatbot 🤖")

  #message("Hello, how are you?")
  #message("I am good", is_user = True)

  with st.sidebar:
    user_input = st.text_input("Your message: ", key = "user_input")
  


if __name__ == "__main__":
  main()
