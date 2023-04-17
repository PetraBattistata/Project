import streamlit as st
import json, requests
from random import choice
from googletrans import Translator

Counter1 = 3
Counter2 = 3

agg_ita1 = ['giovane', 'nuovo', 'presente', 'aperto', 
           'grasso', 'grande', 'caldo', 'chiaro', 
           'occupato', 'amichevole', 'alto', 'lungo' ]

agg_ita2 = ['asciutto', 'conosciuto', 'pericoloso', 'malato', 'morbido', 
           'pesante', 'pieno', 'veloce', 'facile'
           'silenzioso', 'dolce', 'tanto']

agg_ita3 = ['nervoso', 'minuscolo', 'diligente', 'sincero', 'primo', 
          'paziente', 'ordinato', 'presto', 'costoso',
          'interessante', 'coraggioso', 'sazio' ]

translator = Translator()

niveau = st.selectbox('Suche dein Niveau aus!', ('A1', 'A2', 'B1'))

if niveau == 'A1': 
  var = random.choice(agg_ita1)
elif niveau == 'A2': 
  var = random.choice(agg_ita2)
elif niveau == 'B1': 
  var = random.choice(agg_ita3)
st.write(var) 

Adj_cor = translator.translate(var,dest=de)

Adj_deu = st.text_input('Sag mir den Namen des Adjektivs in Deutsch!')

while Counter1 != 0:  
  if Adj_deu == Adj_cor:
    st.write('Richtig!')
  else:
    st.write('Versuch es noch einmal!')
    Counter1 -=1
  if Counter1 == 0:
    st.write('Game over!')
