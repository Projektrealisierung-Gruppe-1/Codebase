# describing the Used models (work in progress)

import streamlit as st
import pandas as pd

def modell_page():
    st.title("Modellinformationen")
    st.write("---")

    st.header("Text Klassifikation")
    c1,c2 =  st.columns([1, 1])
    c1.markdown("""
Bei der Text Klassifikation wurden verschiedene Modelle auf 7 verschiedene Klassen gefintuned.
Folgende Klassen waren dabei enthalten:
- Label_0: Email
- Label_1:  Blog
- Label_2: News
- Label_3: Reviews
- Label_4: Poem
- Label_5: Paper
- Label_6: Recipes""")
    c2.markdown("""
                Der Datensatz für diese wurde händisch von uns zusammengestellt und verschiedene Modelle wurden auf
                diesem getestet. Alle Modelle wurden mit der "Accuracy" (Genauigkeit) bewertet. Folgende Ergbnisse
                kamen bei den verschiedenen Finetunings heraus:""")
    
    c2.table(pd.DataFrame(columns=["Modellname","Accuracy"],data=[["bert-base-uncased",0.979],["xIm-roberta-large",0.988],["microsoft/deberta-base-mnli",0.997]]).set_index("Modellname"))
    st.markdown("""Hierbei wurde sich gegen ein Hyperparameter Tuning entschieden, da die Werte schon extrem gut waren. Das **eigen finegetunte** Modell, des **microsoft/deberta-base-mnli Modells**, wurde dann gespeichert und wird hier in der
                Applikation zur vorhersage der Klasse verwendet.""")
    
    st.header("Sentiment Analyse")
    c1,c2 =  st.columns([1, 1])
    c1.markdown("""
Bei der Sentiment Analyse wurden verschiedene Modelle auf 3 verschiedene "Sentiments" (Gefühle") trainiert und getestet.
Diese Sentiments waren dabei enthalten:
- Label_0: Positiv
- Label_1: Neutral
- Label_2: Negativ
""")
    c2.markdown("""
                Der Datensatz für diese Sentiment Analyse wurde ebenfalls händisch von uns erstellt und gesäubert. Um eine bestmögliche Vorhersage 
                treffen zu können wurden auch hier wieder verschiedene Modelle trainiert. Das Gütekriterium bei diesen Test war auch wieder die  "Accuracy" (Genauigkeit). Folgende Ergbnisse
                wurden erzielt:""")
    
    c2.table(pd.DataFrame(columns=["Modellname","Accuracy"],data=[["ProsusAl/finbert",0.819],["cardiffnlp/twitter-roberta-base-sentiment-latest",0.855],["niptown/bert-base-multilingual-uncased-sentiment",0.816],["siebert/sentiment-roberta-large-english",0.867]]).set_index("Modellname"))
    st.markdown(""" Für unsere Webapplikation wird nun das best getestete Modell, names **siebert/sentiment-roberta-large-english**, verwendet""")

    st.header("Textzusammenfassung")
    st.markdown("""
                Bei der Textzusammenfassung haben wir verschiedene Ansätze getestet. Zunächst einmal das distilbert-base-uncased Modell alleine und dann noch einmal in 
                Kombination mit einem Paraphrasing Modell namens flan-t5-base. Zum Evaluierien der vohergesagten Zusammenfassungen wird als Gütekriterium der Rogue-Score verwendet.
                Die beiden Modelle erzielten folgende Scores:
                """)
    
    st.table(pd.DataFrame(columns=["Modellname","Rogue"],data=[["distilbert-base-uncased",0.177],["distilbert-base-uncased + flan-t5-base","0.194"]]).set_index("Modellname"))
    st.markdown("""Trotz des schlechteren Scores wird in Webapplikation das Modell **distilbert-base-uncased** für die Textzusammenfassung genutzt. Grund hierfür ist die Ausführungszeit. So hat das distilbert-base-uncased 18min
                 für 500 Samples gebraucht und das kombinierte Modell 122min.""")