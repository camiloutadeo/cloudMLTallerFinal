key = "a2e29491463848df825fe0957f48fda7"
endpoint = "https://dectectoridiomatallerfinal.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

import streamlit as st


# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# docs_path = r"/mnt/d/Documentos/camilo/Maestria/Cloud computing/Clase8/Taller_final/Documents/"


st.set_page_config(
    page_title="Detector de lenguaje",  # Setting page title
    page_icon="💬",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded",    # Expanding sidebar by default
    
)

st.header("Deteción de lenguaje 🤖💬🅰️🉐🈴")

response_txt = ''

# Example method for detecting the language of text
def language_detection_example(client, text):
    try:
        response = client.detect_language(documents = [text], country_hint = 'es')[0]
        global response_txt
        response_txt = str(response.primary_language.name)

    except Exception as err:
        print("Encountered exception. {}".format(err))

# language_detection_example(client)


with st.sidebar:
    st.header("Text input")     # Adding header to sidebar
    # Adding file uploader to sidebar for selecting images
    source_txt = st.text_input("Texto a detectar:", key="text")
    st.button("Iniciar deteccion", on_click=language_detection_example(client, source_txt) )
    st.subheader("UTADEO 2023")
    st.subheader("Edward, Ney, Jesus")

if len(source_txt) >0:
    st.subheader(source_txt)
    st.subheader("Lenguaje detectado 🈷️: "+ response_txt)
