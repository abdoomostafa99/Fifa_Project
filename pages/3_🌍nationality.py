import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout = 'wide' , page_title = 'Nationality Page' , page_icon= '🌍')

st.title('Nationality insights')
df = pd.read_csv('fifa_eda.csv')
df.dropna(inplace=True)

st.subheader('Top Country With')
interest =  st.selectbox('Select a column to filter by :',
             ['Skill Moves' , 'Value'])
top_value = df[['Nationality' , interest]].sort_values(by = interest , ascending= False).head(5)
st.plotly_chart(px.bar(top_value , x ='Nationality' , y = interest, color= 'Nationality'))

nationality = st.selectbox('choice nation',df['Nationality'].unique())
number_of_player = df[df['Nationality'] == nationality]['Name'].count()
c1 = st.container(border=1)
c1.subheader(f'{nationality} has ({number_of_player}) players in fifa19 in different clubs')

col1 , col2 , col3 = st.columns(3)
with col1:
    card1 = col1.container(border=1)
    Skill_Moves = df[df['Nationality'] == nationality].nlargest(1, 'Skill Moves').head(1)
    card1.subheader(f'Most Skill Moving Player in {nationality}')
    card1.metric(Skill_Moves['Name'].iloc[0], Skill_Moves['Skill Moves'].iloc[0])

with col2:
    card2 = col2.container(border=1)
    Value = df[df['Nationality'] == nationality].nlargest(1, 'Value').head(1)
    card2.subheader(f'Most Valued Player in {nationality}')
    card2.metric(Value['Name'].iloc[0], Value['Value'].iloc[0])

with col3:
    card3 = col3.container(border=1)
    Overall = df[df['Nationality'] == nationality].nlargest(1, 'Overall').head(1)
    card3.subheader(f'Best Overall Player in {nationality}')
    card3.metric(Overall['Name'].iloc[0], Overall['Overall'].iloc[0])

c1 , c2 = st.columns(2)
with c1 :
    one = c1.container(border=1)
    Age = df[df['Nationality'] == nationality].nlargest(1, 'Age').head(1)
    one.subheader(f'Oldest Age Player in {nationality}')
    one.metric(Age['Name'].iloc[0], Age['Age'].iloc[0])
with c2 :
    two = c2.container(border=1)
    Age = df[df['Nationality'] == nationality].nsmallest(1, 'Age').head(1)
    two.subheader(f'Youngest Age Player in {nationality}')
    two.metric(Age['Name'].iloc[0], Age['Age'].iloc[0])

st.divider()
interest = st.selectbox('Select a column to filter by average in club:',
             ['Age' , 'Overall','Potential','Value','Wage','Skill Moves'])

m1 , m2 = st.columns(2)
with m1:
    maxx = df[df['Nationality'] == nationality][interest].max()
    name = df[df[interest] == maxx]['Name'].iloc[0]
    bord1 = m1.container(border=1)
    bord1.subheader(f'max {interest} in {nationality} ({maxx}) \n{name}')

with m2:
    
    minn = df[df['Nationality'] == nationality][interest].min()
    name = df[df[interest] == minn]['Name'].iloc[0]
    bord2 = m2.container(border=1)
    bord2.subheader(f'min {interest} in {nationality} ({minn}) \n{name}')

avg = df[df['Nationality'] == nationality][interest].mean()
# st.title(f'Average {interest} in {nationality} {avg.round(2)}')

fig = px.bar(df[df['Nationality'] == nationality], x='Name', y=interest, color='Name', text_auto=True)
fig.add_hline(y=avg ,annotation_text=f'Average {interest}: {avg.round(2)}')
st.plotly_chart(fig)
