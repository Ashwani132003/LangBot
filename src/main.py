import streamlit as st

from streamlit_option_menu import option_menu

import firebase_admin

from firebase_admin import credentials, initialize_app, storage, firestore


# import streamlit.components.v1 as components

st.set_page_config(
        page_title="LangBot",
        page_icon=":pencil:",
        layout="wide",
        initial_sidebar_state="expanded",
)


cred = credentials.Certificate("streamlitchat-a40f7-6ae30ae1b5c6.json")
# check if the app is already initialized
try:
    firebase_admin.get_app()
except ValueError as e:
    # if not, then initialize it
    initialize_app(cred, {'storageBucket': 'streamlitchat-a40f7.appspot.com'})



payments = []


class global_state:
    def __init__(self):
        self.email = ''
        self.messages=[]
        self.selectbox=''

if "global_state" not in st.session_state:
    st.session_state.global_state = global_state()

global_state = st.session_state.global_state
