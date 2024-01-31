import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Vicky :sparkles:')
st.subheader(Plot')

x = np.linspase(-2 * np.pi, 1000) # Generating x values from -2*
y = np.sin(x) # Calculating sin(x) values
z = np.cos(x) # Calculating sin(x) values

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b') # Plotting sin (x) curve
ax.plot(x, y, label='cos(x)', color='b') # Plotting sin (x) curve
ax.set_ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabelas(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelssize=15)

st.puplot(fig)
