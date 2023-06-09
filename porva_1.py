from random import choice
import json,requests
import streamlit as st
from googletrans import Translator

st.title('Adjectives')

if 'counter1' not in st.session_state or 'counter2' not in st.session_state :
 st.session_state.counter1 = 3
 st.session_state.counter2 = 3
if st.session_state.counter1 == 0 or st.session_state.counter2 == 0:
 st.title('Game Over!')
 st.stop()

words = ['forte','alto','ricco','pieno','brutto']
if 'choice' not in st.session_state:
 st.session_state.choice = choice(words)
translator = Translator()
trans = translator.translate(st.session_state.choice,src='it', dest= 'en')
if 'word_trans' not in st.session_state:
 st.session_state['word_trans'] = trans.text
if 'correct_word' not in st.session_state:
     st.session_state.correct_word = 0
  
def new_word(new_word):
 st.session_state.choice = new_word
 new_trans = translator.translate(new_word,src='it', dest= 'en')
 st.session_state.word_trans = new_trans.text

 
 
start_word = st.write(st.session_state.choice)


#word_input.text_input('inserisci la tua traduzione:')
word_input = st.text_input('inserisci la tua traduzione:','')
st.write('Tentativi rimasti:',st.session_state.counter1)
  
if word_input:
 if st.session_state.word_trans != word_input:
  st.session_state.counter1 -=1
  st.write('Sbagliato!')
 elif st.session_state.word_trans == word_input:
  st.write('Tentativi rimasti per Antonimi:',st.session_state.counter2)
  word_ant=st.text_input('Esatto! Ora passiamo agli antonimi: ','')
  url= 'https://api.datamuse.com/words?rel_ant=' + st.session_state.word_trans + ''
  response = requests.get(url)
  datamuse = json.loads(response.text)
  if 'antonym' not in st.session_state:
   st.session_state.antonym = datamuse[0]['word']
  st.write(st.session_state.antonym)
  if word_ant:
   if word_ant != st.session_state.antonym:
    st.session_state.counter2 -=1
    st.write('Sbagliato!')
   elif word_ant == st.session_state.antonym:
    st.write('Esatto!')
    word_input = st.empty()
    new_word(choice(words))
    start_word = st.write(st.session_state.choice)
    st.session_state.correct_word +=1
    

st.write(st.session_state.correct_word)

