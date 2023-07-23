import streamlit as st

from welcomepage import welcome_page
from textverarbeitung import text_page
from modellinfo import modell_page
from speech_to_text import speech_to_text_page
from accessability_contrast import accessability_page

st.set_page_config(
    page_title = "Projektrealisierung",
    layout="wide"
    )

# displays a header and a list of available pages.
def draw_all(key,plot=False):
    st.write("""
    # Projektrealisierungs Frontend

    ## Folgende Pages können gefunden werden
    1. Textverarbeitung
    2. Modellinformationen

    """)

with st.sidebar:
    draw_all("sidebar")

# entry point of the application for displaying the different pages
def main():
    menu = ["--select--", "Textverarbeitung",  "Modellinformationen", "Speech-to-text", "Accessability"]
    page = st.sidebar.selectbox("Choose your page:", menu)

    if page =="--select--":
        welcome_page()
    
    elif page == "Textverarbeitung":
        text_page()
    
    elif page == "Modellinformationen":
        modell_page()

    elif page == "Speech-to-text":
        speech_to_text_page()
        
    elif page == "Accessability":
        accessability_page()


if __name__ == "__main__":
    main()