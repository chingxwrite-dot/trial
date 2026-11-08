import streamlit as st

#|Game Interface|
st.set_page_config(page_title = "Game", page_icon="👋") #please add icon 

st.markdown("# the game interface inserted here") #the user panel 

with st.sidebar:
  st.header("MoCA Game") 
#the game insert here #see if only game flow part put here is ok or not
  st.markdown("Participant Information") #the markdown in panel of that page 
  st.text_input("Participant ID", "P001", key="pid")
  st.text_input("Participant Name", "000", key="pid")

