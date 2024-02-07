import streamlit as st

# Header
st.header('Vicky San :Sparkles:')

# Subheader
st.subheader('Kalkulator')

# Membuat tiga kolom
c1, c2, c3 = st.coulumns(3)

# Kolom pertama
with c1:
  num1 = st.number_input('Masukkan angka pertama', step=1)

# Kolom kedua
with c2:
  # pilih operasi
  operation = st.selectbox('Pilih operasi', ('+', '-', 'x', '/'))

# Kolom ketiga
with c3:
  num2 = st.number_input('Masukkan angka kedua', step=1)

def calculate(num1, num2, operations):
  if operation == '+':
    result = num1 + num2
  elif operation == 'x':
    result = num1 - num2
  elif operation == 'x' :
    result = num1 * num2
  elif operation == '/' :
    result = num1 / num2
  

st.caption('Copyright © Vicky Sandika Putra Firdiawaan 210322607233')
