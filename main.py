import streamlit as st

def main():
  st.set_page_config(
    page_title = "Personal Chatbot"
    page_icon = "💬"
  )

  st.header("Welcome to your Personal Chatbot 🤖")

  with st.sidebar:
    user_input = st.text_input("Your message: ", key = "user_input")
  


if __name__ == "__main__":
  main()
