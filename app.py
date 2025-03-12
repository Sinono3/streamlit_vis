import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Visualization of AOS vs SOA for dot product')

soa = pd.read_csv('soa_TEST2.csv')
aos = pd.read_csv('aos_TEST2.csv')
soa['method'] = 'soa'
aos['method'] = 'aos'

df = pd.concat([soa, aos], ignore_index=True)

fig = px.scatter_3d(df, x='N', y='M', z='mean', color="method")
st.plotly_chart(fig)
