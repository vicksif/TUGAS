import streamlit as st

# Header
st.header('Vicky San :Sparkles:')
st.subheader('Plot')

c1, c2 = st.coulumns(2)

with c1:
  x = st.number_imput('Suhu',value=100)
  st.write('=>: ')
with c2:
  satuan = st.selectbox(
    'Satuan',
    ('+', '-', 'x', ':'),key='k1')
  st.werite(':sparkles: ')

st.write(x,' ',satuan,' = ',' ')

st.caption('Copyright © Vicky Sandika Putra Firdiawaan 210322607233')
