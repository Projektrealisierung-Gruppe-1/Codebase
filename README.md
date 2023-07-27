# Projektrealisierung_Gruppe_1
Projektrealisierung Application Respository (Abgabe: Joshua Brenzinger, Constantin Rech, Pascal Breucker und Luis Steinert)

Entwicklung eines NLP Tools zur Textzusammenfassung, Textkategorisierung und Stimmungsanalyse.

---
## Folderstructure:

Evaluation/
  - `hf_classification`: Dateien für Klassifikationsmodell
  - `hf_sentiment`: Dateien für Sentimentanalyse
  - `summeval`: Dateien für Zusammenfassung

Exploration/
  - `classification_exploration.ipynb`:
  - `sentiment_exploration.ipynb`:
  - `summarization_exploration.ipynb`:

webapplikation/
  - `app.py`: Hauptfile der Webapplikation, wird durch Streamlit aufgerufen und gestartet
  - `other files`: Weitere Funktionalitäten und Anwendungsseiten, die durch das Hauptscript aufgerufen werden (e.g. classification.py o. welcomepage.py)

Testdata/
  - Dieser Ordner enthält Testdatensätze in verschiedenen Dateitypen, die zur Evaluierung und zum Testen der verschiedenen Modelle und Funktionen der Web-Applikationen dienen.

## Run this Application
`cd webapplikation/`

`streamlit run app.py`

## Abgabe 

Siehe die finale Abgabe der Dokumente (Präsentation, Dokumentation und Abschlussbericht) **Abgabe-MS-3** https://github.com/Projektrealisierung-Gruppe-1/Abgabe-MS-3
