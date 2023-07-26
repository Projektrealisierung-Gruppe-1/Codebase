# /webapplikation/Dockerfile

FROM python:3.7

WORKDIR /app

RUN git clone https://github.com/Projektrealisierung-Gruppe-1/Codebase.git .

RUN pip install -r requirements_test.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"] 