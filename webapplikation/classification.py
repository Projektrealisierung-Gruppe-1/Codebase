from transformers import pipeline, AutoTokenizer
import streamlit as st

def classfier(text):
    class_model_path = "bert-base-uncased"
    tokenizer=AutoTokenizer.from_pretrained(class_model_path,use_fast=False)
    class_task = pipeline("text-classification", model=class_model_path, tokenizer=tokenizer)

    predict = class_task(text)[0]['label']

    return predict

def sentiment(text):
    sentiment_model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer=AutoTokenizer.from_pretrained(sentiment_model_path,use_fast=False)
    sentiment_task = pipeline("sentiment-analysis", model=sentiment_model_path, tokenizer=tokenizer)

    preddict = sentiment_task(text)[0]
    print(preddict["score"])
    prob = round(preddict["score"]*100,2)
    print(prob)
    pred = preddict["label"]

    return prob, pred