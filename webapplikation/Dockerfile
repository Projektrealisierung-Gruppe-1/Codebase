# /webapplikation/Dockerfile

FROM python:3.10

WORKDIR /app

RUN git clone https://github.com/Coreprog/PR_Frontend.git .

RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"] 