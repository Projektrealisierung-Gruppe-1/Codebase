import streamlit as st
from classification import classfier,sentiment,txtsummary
import docx2txt
# import textract
import pandas as pd
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
import deepl

from transformers import pipeline
from st_custom_components import st_audiorec
import streamlit as st
import os


def text_page():
    
    st.title("Textverarbeitung")
    st.write("---")
    st.header("Text Gegebenheit")

    optch = st.radio(
        "Dateneingabe",
        ["Textfeld", "Dateiupload","Speech to Text"],
        horizontal=True,
    )

    st.write("---")

    if optch == "Dateiupload":
        txt = ""
        uploaded_file = st.file_uploader("Choose a file",accept_multiple_files=False,type=['docx', 'pdf', 'txt','doc'])
        if uploaded_file is not None:
            st.write(uploaded_file.type)
            st.write(uploaded_file.name)
            
            st.write(uploaded_file.name[-3:])
            # check uploaded file for data type
            if "ocx" in uploaded_file.name[-3:]:
                st.write("docx erkannt")   

                txt = docx2txt.process(uploaded_file)
                st.write(txt)
                
                
            if "doc" in uploaded_file.name[-3:]:
                st.write("doc erkannt")


            if "pdf" in uploaded_file.name[-3:]:
                st.write("pdf erkannt")           
 
                reader = PdfReader(uploaded_file)
                for i in range(len(reader.pages)):
                    content = reader.pages[i].extract_text()
                    txt = txt + content
                st.write(txt) 
                
                
            if "txt" in uploaded_file.name[-3:]:
                st.write("txt erkannt")  

                for line in uploaded_file:
                    txt = txt + "\n" + line.decode("utf-8")
                st.write(txt)
                

    elif optch == "Textfeld":
        txt = st.text_area("Your text:",key= "NLP")
        load_dotenv()
        DEEPLKEY = os.getenv("DEEPLKEY")
        translator = deepl.Translator(DEEPLKEY)
        target_language = "EN-US"
    
        if txt != "":
            txt = str(translator.translate_text(txt, target_lang=target_language))
            if txt != "":
                st.write(f"""Der eingegebene Text auf Englisch ist: \\
                        {txt}""")
    

    elif optch == "Speech to Text":
        txt = ""

        wav_audio_data = st_audiorec()

        if wav_audio_data is not None:

            if os.path.isfile('webapplikation/audio.wav'):
                with open('webapplikation/audio.wav', mode='bw') as f:
                    f.write(wav_audio_data)
            # Your error handling goes here
            else:
                with open('webapplikation/audio.wav', mode='bx+') as f:
                    f.write(wav_audio_data)
            
            pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")
            txt = pipe("webapplikation/audio.wav")["text"]
            st.write(txt)
        
    
    
    # translate logic
    # load dotenv secrets

    
    

    crate = st.slider('Kompressionsrate', 20, 80, 60)

    st.write("---")
    st.header("Analyse des Textes")

    if txt != "":
        st.subheader("Text Zusammenfassung")
        with st.spinner('Text wird zusammengefasst...'):
                        zsm_txt = txtsummary(txt,crate/100)
        st.write(zsm_txt)

        st.markdown("""
                    

        """)
        
        st.subheader("Klassifizierungen")

        #if     

        c1,c2 =  st.columns([1, 1])

        c1.markdown("**Text Klassifzierung**")
        with st.spinner('Classification wird durchgeführt...'):
            txtpred = classfier(zsm_txt)
        c1.write(f"Der Text ist aus der Kategorie {txtpred}.")

        c2.markdown("**Sentiment Analyse**")
        with st.spinner('Sentiment Analyse wird durchgeführt...'):
                        prob, pred = sentiment(zsm_txt)
        c2.write(f"Mit einer Wahrscheinlichkeit von {prob}% sagt das Modell voraus, dass dieser Text {pred} ist.")

        
    else:
         st.write("Es wurde noch keine Datei hochgeladen.")
    

    st.write("---")
    st.header("Download der Ergebnnisse")
    st.subheader("Welche Ergebnisse sollen im Download sein")
    col1, col2 = st.columns([1, 1])
    
    d1 = col1.checkbox("Text Resort")
    d2 = col1.checkbox("Text Sentiment")
    d3 = col1.checkbox("Text Zusammenfassung")

    if d1 != False or d2 != False or d3 != False:
        genre = col2.radio(
        "Dateiformat",
        ('docx', 'pdf', 'txt'))

        text_contents = '''This is some text'''
        st.download_button('Download Zusammenfassung', text_contents)




