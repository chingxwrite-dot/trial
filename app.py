import streamlit as st
import os

st.set_page_config(page_title="MoCA", page_icon="🎮", layout="wide")

# 2. Authentication (if you have auth.py in your folder)
# from auth import login_gate, logout_button
# login_gate()
# logout_button()

# 3. Build the Sidebar
st.sidebar.header("Game")

# 4. Define the pages (This creates the navigation menu!)
pages = {
    "User": [
        st.Page("pages/game.py", title="Game", icon="🕹️"),
    ],
    "Admin": [
        st.Page("pages/admin.py", title="Admin / Tester", icon="⚙️"),
    ],
}

# 5. Run the router
nav = st.navigation(pages)
nav.run()
