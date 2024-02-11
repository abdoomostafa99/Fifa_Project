import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout = 'wide' , page_title = 'Home Page' , page_icon= '🏠')

st.title('Fifa 19 Data Analysis')
st.image('https://i.ytimg.com/vi/zX0AV6yxyrQ/maxresdefault.jpg')
df = pd.read_csv('fifa_eda.csv')
df.dropna(inplace=True)

st.markdown('''
Welcome To Fifa 19 Data Analysis\n
This app allows you to explore the data of FIFA 19 game by EA Sports. You can filter and search for players, see their stats, and even predict their potential value in a future
\nthis is resourse data from [kaggle]('https://www.kaggle.com/datasets/javagarm/fifa-19-complete-player-dataset)
''')

st.subheader('Sample Dataset')
if st.checkbox('Show Dataset'):
    st.dataframe(df.head(10))