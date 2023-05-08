import streamlit as st
import json, requests
import random
from googletrans import Translator


st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 3

    #agg_ita1
    
increment = st.button('Increment')
if increment:
    st.session_state.count -= 1

st.write('Count = ', st.session_state.count)
if st.session_state.count <= 0:
    st.write('Game over!')
    st.stop()
