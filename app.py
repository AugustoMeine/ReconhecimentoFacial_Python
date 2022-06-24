import streamlit as st 

arvore = pickle.load(open("arvoreSalva.sav",'rb'))

p1 = st.selectbox(
     'Escolha uma das opções', 
     ('1', '2', '3'))

st.write('Voce escolheu:', p1)

st._input ("test",key='var')