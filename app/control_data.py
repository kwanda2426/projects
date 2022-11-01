import streamlit as st
import pandas as pd
from pages import login, signup, custom_model # import your app modules here
from db_func import *
from session_state import _get_state

# Hide mainmenu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



def main():
    state = _get_state()

    state.page_config = st.set_page_config(page_title="ABC", layout="wide", initial_sidebar_state="expanded")

    pages = {
        "Login": login.app,
        "Signup": signup.app,
        "Custom Model": custom_model.app,
    }

    st.sidebar.title(":floppy_disk: Page states")
    page = st.sidebar.selectbox("Select Page", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page](state,st)
    
    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    state.sync()

if __name__ == "__main__":
    main()


