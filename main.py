import streamlit as st
import pandas as pd
import numpy as np

with open("style.css" ) as css: #"app\style.css"
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.title('Uber pickups in NYC')

st.write('tre')