import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Temperature")

dataframe = pd.read_csv("temperature.txt")
# print(dataframe)

X=[]
Y=[]
for index, item in dataframe.iterrows():
    X.append(item["datetime"])
    Y.append(item[" temperature"])

# print("X: ", X)
# print("Y: ", Y)

figure = px.line(x=X, y=Y, labels={"x":"Date-Time", "y":"Temperature(C)"})
st.plotly_chart(figure)
