from transformers import pipeline, AutoTokenizer
import streamlit as st
from summarizer import Summarizer

@st.cache_data(show_spinner=False)
def classfier(text):
    class_model_path = "bert-base-uncased"
    tokenizer=AutoTokenizer.from_pretrained(class_model_path,use_fast=False)
    class_task = pipeline("text-classification", model=class_model_path, tokenizer=tokenizer)

    predict = class_task(text)[0]['label']

    return predict

@st.cache_data(show_spinner=False)
def sentiment(text):
    sentiment_model_path = "siebert/sentiment-roberta-large-english"
    tokenizer=AutoTokenizer.from_pretrained(sentiment_model_path,use_fast=False)
    sentiment_task = pipeline("sentiment-analysis", model=sentiment_model_path, tokenizer=tokenizer)

    preddict = sentiment_task(text)[0]
    prob = round(preddict["score"]*100,2)
    pred = preddict["label"]

    return prob, pred

@st.cache_data(show_spinner=False)
def txtsummary(text, crate):
    model = Summarizer('distilbert-base-uncased')
    zsm_text = model(text, ratio=crate)

    return zsm_text