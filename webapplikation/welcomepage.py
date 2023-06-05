import streamlit as st

def welcome_page():
    st.title("Welcome Page")
    st.write("---")
    st.markdown(""" 
                In dieser Web Applikation werden Funktionen zur Klassifizierung von Nachrichtenartikeln geboten. Hier kann das Resort sowie das Senitment des Artikels bestimmt werden.
                Des Weiteren besteht die Möglichkeit alle Artikel, welche via pdf, txt oder word Dateiformat hochgeladen werden oder in der Texteingabe formuliert werden, zusammengefasst werden.
                Hierbei kann die Kompressionsrate vom Benutzer festgelegt. Die Ausgabe der Zusammenfassung erfolgt dabei in der Sprache vom Original Dokument.
                """)
                
