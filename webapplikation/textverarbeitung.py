import streamlit as st
from classification import classfier,sentiment
from speech_to_text import transcribe_audio_imp


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
        uploaded_file = st.file_uploader("Choose a file",accept_multiple_files=False,type=['docx', 'pdf', 'txt'])

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





