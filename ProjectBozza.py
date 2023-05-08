import streamlit as st
import json, requests
import random
from googletrans import Translator


st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 3

Adj_cor = translator.translate(var,dest='en')
Adj_eng = st.text_input('Tell me the name of this adjective in english!','')
    #agg_ita1

    
if st.session_state.count <= 0:
    st.stop()
increment = st.button('Increment')
if Adj_eng != Adj_cor.text:
    st.write('Try again stupido!')
    st.session_state.count -= 1 
elif Adj_eng.text == Adj_cor.text:
    st.write('right!')

st.write('Count = ', st.session_state.count)
if st.session_state.count <= 0:
    st.write('Game over!')

