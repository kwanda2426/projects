import streamlit as st
import pandas as pd


# Hide mainmenu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



def main():
    

    page_config = st.set_page_config(page_title="ABC", layout="wide", initial_sidebar_state="expanded")


    st.sidebar.title(":floppy_disk: Page states")
    page = st.sidebar.selectbox("Select Page")

 


if __name__ == "__main__":
    main()


