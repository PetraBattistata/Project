import streamlit as st
import json, requests
import random
from googletrans import Translator


st.title('Counter Example')
if 'Counter1' not in st.session_state:
    st.session_state.Counter1 = 3

increment = st.button('Increment')
if increment:
    st.session_state.Counter1 -= 1

st.write('Count = ', st.session_state.count)
