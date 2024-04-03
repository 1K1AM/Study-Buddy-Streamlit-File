import streamlit as st
import datetime

add_selectbox = st.selectbox(
  "Choose Subject:",
  ("Programming", "Biology", "Chemistry", "Spanish", "Calculus")
)

st.divider()

st.markdown('''⁣⁣⁣⁣⁣⁣ ⁣ ⁣⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣⁣⁣ ⁣ ⁣ ⁣ ⁣ ⁣ ⁣Message M:red[AI]TE''')

with st.container(height=580, border=True):
  with st.chat_message("MAITE", avatar="🤖"):
    st.write("Hello")

prompt = st.chat_input("Message MAITE...")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

with st.sidebar:
  st.date_input("Search by day", value = None)
  st.divider()
  st.text("Today") 
  st.text_area("",key=1)
  st.text("Yesterday") 
  st.text_area("",key=2)
  st.text("Past Week") 
  st.text_area("",key=3)

