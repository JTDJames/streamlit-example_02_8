import streamlit as st
import pandas as pd
import numpy as np
import joblib

from PIL import Image

st.sidebar.title('Sidebar')

st.title('This is a title')

st.image('images/penguins.jpg', use_column_width='always')

col1, col2, = st.columns(2)
col1.subheader('Col1')
col2.header('Col2')

col21, col22, col23 = st.columns([3,2,1])

col21.write('Wide column, text will wrap testing 1234')
col22.write('Middle')
col23.write('small')

button1 = st.button('Click me')

if button1:
    st.write('Button was clicked')