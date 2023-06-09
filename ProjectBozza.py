import streamlit as st
import json, requests
import random
from googletrans import Translator


st.title('Adjectives')
if 'count' not in st.session_state:
    st.session_state.count = 4
if st.session_state.count <= 1:
    st.title('Game Over!')
    st.stop()


st.button('Start')

if 'Start':    
    agg_ita1 = ['giovane', 'nuovo', 'aperto', 
                'grande', 'caldo', 
                'amichevole', 'alto', 'lungo' ]

    agg_ita2 = ['bagnato', 'conosciuto', 'pericoloso', 'sano', 'morbido', 
                'pesante', 'pieno', 'veloce', 'facile'
                'silenzioso', 'dolce']

    agg_ita3 = ['nervoso', 'minuscolo', 'diligente', 'sincero', 'primo', 
                'paziente', 'ordinato', 'presto', 'costoso',
                'interessante', 'coraggioso', 'sazio' ]

    translator = Translator()

    niveau = st.selectbox('Choose your Level!', ('A1', 'A2', 'B1'))
    var = ''


    if niveau == 'A1': 
        var = random.choice(agg_ita1)
    elif niveau == 'A2': 
        var = random.choice(agg_ita2)
    elif niveau == 'B1': 
        var = random.choice(agg_ita3)
    else:
        pass
    st.write(var) 

    Adj_cor = translator.translate(var,dest='en')
    Adj_eng = st.text_input('Tell me the name of this adjective in english!','')
    #agg_ita1
    st.write(Adj_cor.text)
    

    if Adj_eng != Adj_cor.text:
        st.write('Try again stupido!')
        st.session_state.count -= 1 
    elif Adj_eng == Adj_cor.text:
        st.write('right!')
        st.session_state.count += 1 

st.write('Count = ', st.session_state.count)
#if st.session_state.count <= 1:
    #st.write('Game over!')

