import streamlit as st
from classification import classfier,sentiment
from speech_to_text import transcribe_audio_imp
from io import StringIO
import docx2txt
import textract
import pandas as pd
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
import deepl


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
                txt = ""
                for i in range(len(reader.pages)):
                    content = reader.pages[i].extract_text()
                    txt = txt + content
                st.write(txt) 
                
                
            if "txt" in uploaded_file.name[-3:]:
                st.write("txt erkannt")  
                txt = ""
                for line in uploaded_file:
                    txt = txt + "\n" + line.decode("utf-8")
                st.write(txt)
                
    elif optch == "Textfeld":
        txt = st.text_area("Your text:",key= "NLP")

    elif optch == "Speech to Text":
        txt = ""
        start_recording = st.button("Start Recording")
        stop_recording = st.button("Stop Recording")

        if start_recording:
            with st.spinner('Bitte sprechen, Text wird erkannt...'):      
                st.session_state.stop_recording = False
                txt = transcribe_audio_imp()

        if stop_recording:
            st.session_state.stop_recording = True
        if txt == "":
            pass
        else:
            st.write(f"Der erkannte Text ist: {txt}")
    
    
    
    # translate logic
    # load dotenv secrets
    load_dotenv()
    DEEPLKEY = os.getenv("DEEPLKEY")
    translator = deepl.Translator(DEEPLKEY)
    target_language = "EN-US"
    
    txt_english = translator.translate_text(txt, target_lang=target_language)
    if txt_english != "":
        st.write(f"Der übersetzte Text ist: {txt_english}")
    
    
    

    age = st.slider('Kompressionsrate', 20, 80, 60)

    st.write("---")
    st.header("Analyse des Textes")
    st.subheader("Klassifizierungen")

    if txt != "":
        c1,c2 =  st.columns([1, 1])

        c1.markdown("**Text Klassifzierung**")
        with st.spinner('Classification wird durchgeführt...'):
            txtpred = classfier(txt)
        c1.write(f"Der Text ist aus der Kategorie {txtpred}.")

        c2.markdown("**Sentiment Analyse**")
        with st.spinner('Sentiment Analyse wird durchgeführt...'):
                        prob, pred = sentiment(txt)


        c2.write(f"Mit einer Wahrscheinlichkeit von {prob}% sagt das Modell voraus, dass dieser Text {pred} ist.")

        st.subheader("Text Zusammenfassung")
        st.text("....")
    

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





