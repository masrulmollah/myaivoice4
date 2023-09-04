import pandas as pd
import pyttsx3
import speech_recognition as sr
import streamlit as st

df2 = pd.read_csv('freshcsv.csv', index_col="Name")

r = sr.Recognizer()

st.title("Voice-Activated Data Lookup")

while True:
    my_ask1 = None  # Initialize my_ask1 as None
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        st.write("Ask your question..")
        audio = r.listen(source)

        try:
            st.write(r.recognize_google(audio))
            voiceInput = r.recognize_google(audio)

        except Exception as e:
            st.error("Error..." + str(e))

        if voiceInput == "close":
            st.write("Bye for now!!!")
            break  # Exit the loop if the user says "close"

        try:
            my_ask1 = df2.loc[voiceInput]
        except KeyError:
            st.warning("Invalid Command! Please ask me again")

        if my_ask1 is not None:  # Check if my_ask1 is not None
            for Name, value in df2.items():
                st.write(value[0])

            alexa = pyttsx3.init()
            voices = alexa.getProperty('voices')
            alexa.setProperty('voice', voices[1].id)
            
            # Check if my_ask1 is empty before attempting to access its elements
            if not my_ask1.empty:
                alexa.say(list(my_ask1)[0])
                alexa.runAndWait()
