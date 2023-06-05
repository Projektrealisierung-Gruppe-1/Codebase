import streamlit as st



def text_page():
    
    st.title("Textverarbeitung")
    st.write("---")
    st.header("Text Gegebenheit")
    
    uploaded_file = st.file_uploader("Choose a file",accept_multiple_files=False,type=['docx', 'pdf', 'txt'])
    st.write("oder")
    txt = st.text_area("Your text:",key= "NLP")



    age = st.slider('Kompressionsrate', 20, 80, 60)

    st.write("---")
    st.header("Analyse des Textes")
    st.subheader("Klassifizierungen")

    c1,c2 =  st.columns([1, 1])

    c1.markdown("**Resort Klassifzierung**")
    c1.write("...")

    c2.markdown("**Sentiment Analyse**")
    c2.write("...")

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
        ('PDF', 'Wordx', 'txt'))

        text_contents = '''This is some text'''
        st.download_button('Download Zusammenfassung', text_contents)





