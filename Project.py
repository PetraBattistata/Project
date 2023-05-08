import streamlit as st
import json, requests
import random
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

if Adj_eng is not None:
           if Counter1 > 0:
                      if Adj_eng == Adj_cor:
                                 st.write('Right!')
                      if not Adj_eng == Adj_cor:
                                 st.write('Try again!')
                                 Counter1 -= 1
           elif Counter1 <= 0:
                      st.write('Game over!')
           else:
                      pass
#'Now tell me the anthonym of this word!' 
           
                      
