import streamlit as st

def welcome_page():
    st.title("Willkommen")
    st.write("---")
    st.markdown(""" 
                1. **Textverarbeitung**: Diese Web Applikation ist das Ergebnis eines Projektes des Faches Projektrealisierung. In dieser Web-App sind 
                Funktionen zur Klassifizierung von Text geboten. Außerdem wird das Sentiment des Textes analysiert. Auch eine Textzusammenfassung mit einer eigen
                bestimmten Kompressionsrate wird geboten. Alle Texte können via Textfeld, Dateiupload (pdf, txt oder docx) oder Speech2Text hochgeladen werden. Diese
                Texte können in beliebiger Sprache bereitgestellt werden und von der Web-App verarbeitet werden. Wenn die Analysen getätigt worden sind können die Ergebnisse
                dieser sich als pdf, txt oder docx gedownloadet werden. Die Zusammenfassung dieses Textes kann in verschieden Sprachen ausgeben werden. Möglichkeiten sind hierbei
                Deutsch, Englisch, Franzözisch, Italienisch oder Spanisch. \n
                2. **Modellinformationen**: Außerhalb der Textverarbeitung kann der User sich innerhalb des Sektors Modellinformationen noch Hintergründe zu den Modellen abholen. \n
                3. **Accessability**: Im Bereich der Accessability kann der User sich die Website gemäß des internationalen Standards zur barrierefreien Gestaltung von Internetangeboten des World Wide Web Consortiums ( W3C ) konfigurieren.
                Hierbei können Anpassung an Primary Color, Text Color, Background Color und Secondary Background Color getätigt werden.
                
                """)
                
