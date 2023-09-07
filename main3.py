from bardapi import Bard
import os
import streamlit as st
from streamlit_chat import message
import speech_recognition as sr

os.environ["_BARD_API_KEY"] = 'agj4A9vqM3wO36Xh_Z6LVlu_IGg6YdJcw4UxLLMLN064OXKFlebMKFNQ4E22m7Ivume3UA.'

st.title("HackVisionaRies Navigation Assistance")

def response_api(prompt):
    message = Bard().get_answer(str(prompt))['content']
    return message

def user_input():
    input_text = st.text_input("Enter Your Prompt:")
    return input_text

# Create a function to capture audio input and convert it to text
def capture_audio():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        st.write("Speak your prompt...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        st.write("Processing audio...")
        user_text = recognizer.recognize_google(audio)
        return user_text
    except sr.UnknownValueError:
        st.write("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        st.write(f"Could not request results; {e}")
        return None

if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

voice_input_button = st.button("Speak Your Prompt")
if voice_input_button:
    user_text = capture_audio()
    if user_text:
        output = response_api(user_text)
        st.session_state['generate'].append(output)
        st.session_state['past'].append(user_text)

text_input = user_input()
if text_input:
    output = response_api(text_input)
    st.session_state['generate'].append(output)
    st.session_state['past'].append(text_input)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user') 
        message(st.session_state['generate'][i], key=str(i))
