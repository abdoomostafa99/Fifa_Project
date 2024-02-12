import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout = 'wide' , page_title = 'Players Page' , page_icon= '🏃‍♂️')

st.title('Players insights')
df = pd.read_csv('fifa_eda.csv')
df.dropna(inplace=True)

age =  st.selectbox('Select Average Age per :',
             ['Overall' , 'Value' , 'Skill Moves'])
df_country = df.groupby('Age')[age].mean().reset_index()
st.plotly_chart(px.scatter(df_country , x = 'Age' , y = age , title = f'Avg Age per {age}'))

skill = st.selectbox('Select Average Skill Moves per :',
             ['Preferred Foot' , 'Position'])
skill_foot = df.groupby(skill)['Skill Moves'].mean().reset_index()
st.plotly_chart(px.bar(skill_foot , x = skill , y = 'Skill Moves' , color=skill))


st.subheader('Average Age per position')
position_age = df.groupby('Position')['Age'].mean().reset_index()
st.plotly_chart(px.bar(position_age , x = 'Position' , y = 'Age' , color='Position'))


interest = st.selectbox('Select a column to filter by:',
             ['Age' , 'Overall','Potential','Value','Wage','Skill Moves'])

col1 , col2 , col3 = st.columns(3)
card1 = col1.container(border=1)
card1.metric(label = f'Max {interest}' , value = df[interest].max())

card2 = col2.container(border=1)
card2.metric(label = f'Min {interest}' , value = df[interest].min())

card3 = col3.container(border=1)
card3.metric(label = f'Avg Value of {interest}' , value = df[interest].mean().round(3))

interestt = st.selectbox(f'Select {interest} filter by:',
             ['Top','Buttom'])


if interestt == 'Top':
    st.title(f'Top 10 {interest}')
    dfnew = df[['Name','Club',interest]].nlargest(10 , interest)
    st.plotly_chart(px.bar(dfnew , x = 'Name' , y = interest , color='Name' , text_auto = 'True'))

    st.title(f'top 10 {interest}')
    st.markdown(dfnew.to_markdown(index=False))

if interestt == 'Buttom':
     st.title(f'buttom 10 {interest}')
     dfnew1 = df[['Name','Club',interest]].nsmallest(10 , interest)
     st.plotly_chart(px.bar(dfnew1 , x = 'Name' , y = interest , color='Name', text_auto = 'True'))
     
     st.title(f'buttom 10 {interest}')
     st.markdown(dfnew1.to_markdown(index=False))
