import pyaudio
import streamlit as st
import speech_recognition as sr

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
                st.text(transcription_object_1)

                if transcription_object_1 == 'quit':
                    break
            except:
                st.text('Could not understand. Please try again!')
