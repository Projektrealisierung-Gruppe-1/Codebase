# /webapplikation/Dockerfile

FROM python:3.10

WORKDIR /app

RUN git clone https://github.com/Projektrealisierung-Gruppe-1/Codebase.git .

RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y

RUN pip install -r requirements_test.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"] 