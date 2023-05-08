import streamlit as st
import json, requests
import random
from googletrans import Translator

Counter1 = 3
Counter2 = 3

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


while Counter1 > 0:
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
           st.write(Adj_cor)
           Adj_eng = st.text_input('Tell me the name of this adjective in english!','')
           st.write(Adj_eng)
           if Adj_eng:
                      if Adj_eng != Adj_cor:
                                 st.write('Try again!')
                                 Counter1 -= 1
                                 st.write(Counter1)
                      elif Adj_eng == Adj_cor:
                                 st.write('right!')
                                 break
if Counter1 == 0:
           st.write('Game over!')
              
#'Now tell me the antonym of this word!' 
           
                      
