import streamlit as st

from welcomepage import welcome_page
from textverarbeitung import text_page
from modellinfo import modell_page
from speech_to_text import speech_to_text_page
from accessability_contrast import accessability_page

import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# layout config
st.set_page_config(
    page_title = "Projektrealisierung",
    layout="wide"
    )

# authentification / login
# with open('./webapplikation/config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# # create authenticator
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# render login widget+
# decomment next line to enable authentification
# name, authentication_status, username = authenticator.login('Login', 'main')

def word_count(text):
    return len(text.split())


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
    menu = ["--select--", "Textverarbeitung",  "Modellinformationen", "Accessability"]
    page = st.sidebar.selectbox("Choose your page:", menu)

    if page =="--select--":
        welcome_page()
    
    elif page == "Textverarbeitung":
        text_page()
    
    elif page == "Modellinformationen":
        modell_page()

    # elif page == "Speech-to-text":
    #     speech_to_text_page()
        
    elif page == "Accessability":
        accessability_page()


if __name__ == "__main__":
    # change comments to enable authentification
    
    # hide content if not authenticated
    # if authentication_status:
    #     authenticator.logout('Logout', 'main')
    #     st.write(f'Welcome *{name}*')
    #     main()
    # elif authentication_status == False:
    #     st.error('Username/password is incorrect')
    # elif authentication_status == None:
    #     st.warning('Please enter your username and password')
        
    main()

    