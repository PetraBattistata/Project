import streamlit as st
import json, requests
from random import choice
from googletrans import translator

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
  else
    st.write('Versuch es noch einmal!')
    Counter1 -=1
  if Counter1 == 0:
    st.write('Game over!')

    url = https://api.datamuse.com/words?rel_ant=

  
  
gegenteil_cor = 

gegenteil = st.text_input('Sag mir jetzt das Gegenteil!')

while Counter2 != 0:  
  If gegenteil == gegenteil_cor:
    st.write('Richtig!')
  else
    st.write('Versuch es noch einmal!')
    Counter2 -=1
    if Counter2 == 0
    st.write('Game over!')


 #cancellare elemento  dopo averlo usato
    

 #1creare lista agg in italiano
  #2 random choice di agg in ital
  #3 con google trans ottenere la traduzione dell agg in ted
  #4 paragonare input utente con traduzione
  #if correct: haggele, if wrong, try again (2)
  #if correct: API datamuse cerca gegenteil
  # paragonare nuovo input dell'utente a gegenteil
    #if correct: haggele, if wrong, try again (2)
 
