import streamlit as st 

p1 = st.selectbox(
     'Escolha uma das opções', 
     ('1', '2', '3'))

st.write('Voce escolheu:', p1)
