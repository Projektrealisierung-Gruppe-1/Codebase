from transformers import pipeline, AutoTokenizer
import streamlit as st
from summarizer import Summarizer

# Wandelt LABEL_x in eigentliches Label um
def label_converter(label):
    if label == 'LABEL_0':
        return "Email"
    elif label == 'LABEL_1':
        return "Blog"
    elif label == 'LABEL_2':
        return "News"
    elif label == 'LABEL_3':
        return "Reviews"
    elif label == 'LABEL_4':
        return "Poem"
    elif label == 'LABEL_5':
        return "Paper"
    elif label == 'LABEL_6':
        return "Recipes"

# Führt Textkalssifizierung aus
@st.cache_data(show_spinner=False)
def classfier(text):
    class_model_path = "CoReProg/7class_PR"
    tokenizer=AutoTokenizer.from_pretrained(class_model_path,use_fast=False)
    class_task = pipeline("text-classification", model=class_model_path, tokenizer=tokenizer)
    output = class_task(text)
    output[0]["label"] = label_converter(output[0]["label"])
    output[0]["score"] = round(output[0]["score"]*100,2)
    return output[0]["score"],output[0]["label"]

# Führt Textsentiment Analyse aus
@st.cache_data(show_spinner=False)
def sentiment(text):
    sentiment_model_path = "siebert/sentiment-roberta-large-english"
    tokenizer=AutoTokenizer.from_pretrained(sentiment_model_path,use_fast=False)
    sentiment_task = pipeline("sentiment-analysis", model=sentiment_model_path, tokenizer=tokenizer)

    preddict = sentiment_task(text)[0]
    prob = round(preddict["score"]*100,2)
    pred = preddict["label"]

    return prob, pred

# Textzusammenfassung des Textes
@st.cache_data(show_spinner=False)
def txtsummary(text, crate):
    model = Summarizer('distilbert-base-uncased')
    zsm_text = model(text, ratio=crate)

    return zsm_text

# Summarization mit Paraphrasing falsche Kompressionsrate
# @st.cache_data(show_spinner=False)
# def txtsummary2(text, crate):
#     model = Summarizer('distilbert-base-uncased')
#     zsm_text = model(text, ratio=crate)
    
#     zwstxtl = tokenize.sent_tokenize(zsm_text)

#     model_name = "google/flan-t5-base"
#     pipe = pipeline("text2text-generation",model = model_name)
#     output = " ".join([pipe("paraphrase:" + sent)[0]["generated_text"]for sent in zwstxtl])

#     return output