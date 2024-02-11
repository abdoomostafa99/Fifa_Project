import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout = 'wide' , page_title = 'Clubs Page' , page_icon= '⚽')

st.title('Clubs insights')
df = pd.read_csv('fifa_eda.csv')
df.dropna(inplace=True)

top_value = df[['Club' , 'Value' ]].sort_values(by = 'Value' , ascending= False).head(5)
# if st.checkbox('Top Value'):
st.plotly_chart(px.bar(top_value , x = 'Club' , y = 'Value' , color='Club' ,title='Top 5 club with value'))

st.divider()

club = st.selectbox('choice club name',df['Club'].unique())
number_of_player = df[df['Club'] == club]['Name'].count()
c1 = st.container(border=1)
c1.subheader(f'{club} has {number_of_player} players')

col1 , col2 , col3 = st.columns(3)
with col1:
    card1 = col1.container(border=1)
    Skill_Moves = df[df['Club'] == club].nlargest(1, 'Skill Moves').head(1)
    card1.subheader(f'Most Skill Moving Player in {club}')
    card1.metric(Skill_Moves['Name'].iloc[0], Skill_Moves['Skill Moves'].iloc[0])

with col2:
    card2 = col2.container(border=1)
    Value = df[df['Club'] == club].nlargest(1, 'Value').head(1)
    card2.subheader(f'Most Valued Player in {club}')
    card2.metric(Value['Name'].iloc[0], Value['Value'].iloc[0])

with col3:
    card3 = col3.container(border=1)
    Overall = df[df['Club'] == club].nlargest(1, 'Overall').head(1)
    card3.subheader(f'Best Overall Player in {club}')
    card3.metric(Overall['Name'].iloc[0], Overall['Overall'].iloc[0])

c1 , c2 = st.columns(2)
with c1 :
    one = c1.container(border=1)
    Age = df[df['Club'] == club].nlargest(1, 'Age').head(1)
    one.subheader(f'Oldest Age Player in {club}')
    one.metric(Age['Name'].iloc[0], Age['Age'].iloc[0])
with c2 :
    two = c2.container(border=1)
    Age = df[df['Club'] == club].nsmallest(1, 'Age').head(1)
    two.subheader(f'Youngest Age Player in {club}')
    two.metric(Age['Name'].iloc[0], Age['Age'].iloc[0])

st.divider()
   
interest = st.selectbox('Select a column to filter by average in club:',
             ['Age' , 'Overall','Potential','Value','Wage','Skill Moves'])

m1 , m2 = st.columns(2)
with m1:
    maxx = df[df['Club'] == club][interest].max()
    name = df[df[interest] == maxx]['Name'].iloc[0]
    bord1 = m1.container(border=1)
    bord1.subheader(f'max {interest} in {club} ({maxx}) \n{name}')

with m2:
    
    minn = df[df['Club'] == club][interest].min()
    name = df[df[interest] == minn]['Name'].iloc[0]
    bord2 = m2.container(border=1)
    bord2.subheader(f'min {interest} in {club} ({minn}) \n{name}')

avg = df[df['Club'] == club][interest].mean()
# st.title(f'Average {interest} in {club} {avg.round(2)}')

fig = px.bar(df[df['Club'] == club], x='Name', y=interest, color='Name', text_auto=True)
fig.add_hline(y=avg ,annotation_text=f'Average {interest}: {avg.round(2)}')
st.plotly_chart(fig)
