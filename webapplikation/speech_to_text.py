import pyaudio
import streamlit as st
import speech_recognition as sr

# main function for the speech-to-text page. displaying the title of the page and a horizontal line.
def speech_to_text_page():
    st.title("Real-Time Speech-to-text")
    st.write("---")
 
    start_recording = st.button("Start Recording")
    stop_recording = st.button("Stop Recording")

    if start_recording:
        st.session_state.stop_recording = False
        transcribe_audio()

    if stop_recording:
        st.session_state.stop_recording = True

#  initiate speech recognition if button is clicked
def transcribe_audio():
    # initialize
    r = sr.Recognizer()

    while st.session_state.stop_recording == False:
        with sr.Microphone() as source:
            # clear background noise
            r.adjust_for_ambient_noise(source, duration=0.3)
            
            st.text("Recording started... Please speak now")
            # capture the audio
            audio = r.listen(source)
            
            try:
                transcription_object_1 = r.recognize_google(audio)
                print("Das ist der eingegebene Text:", transcription_object_1)
                st.text("Erkannt: ", transcription_object_1)

                if transcription_object_1 == 'quit':
                    break
            except:
                st.text('Could not understand. Please try again!')


def transcribe_audio_imp():
    # initialize
    r = sr.Recognizer()

    while st.session_state.stop_recording == False:
        with sr.Microphone() as source:
            # clear background noise
            r.adjust_for_ambient_noise(source, duration=0.3)
            
            st.text("Recording started... Please speak now")
            # capture the audio
            audio = r.listen(source)
            
            try:
                transcription_object_1 = r.recognize_google(audio)

                if transcription_object_1 == 'quit':
                    break
            except:
                transcription_object_1 = 'Could not understand. Please try again!'
    
    return transcription_object_1
