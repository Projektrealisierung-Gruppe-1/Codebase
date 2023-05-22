import streamlit as st

from welcomepage import welcome_page
from textverarbeitung import text_page
from modellinfo import modell_page


st.set_page_config(
    page_title = "Projektrealisierung",
    layout="wide"
    )

def draw_all(key,plot=False):
    st.write("""
    # Projektrealisierungs Frontend

    ## Folgende Pages können gefunden werden
    1. Text Klassifizierung/ Kompression
    2. Modellinformationen

    """)

with st.sidebar:
    draw_all("sidebar")

def main():
    menu = ["--select--", "Textverarbeitung",  "Modellinformationen"]
    page = st.sidebar.selectbox("Wähle die Page:", menu)

    if page =="--select--":
        welcome_page()
    
    elif page == "Textverarbeitung":
        text_page()
    
    elif page == "Modellinformationen":
        modell_page()


if __name__ == "__main__":
    main()