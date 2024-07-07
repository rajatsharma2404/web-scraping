import streamlit as st
import plotly.express as px
import pandas as pd
import sqlite3

st.title("Temperature")
connection = sqlite3.connect("temperature.db")


def get_date_time():
    cursor = connection.cursor()
    cursor.execute("SELECT date_time FROM temperature")
    result = cursor.fetchall()
    result = [t[0] for t in result]
    return result


def get_temperature():
    cursor = connection.cursor()
    cursor.execute("SELECT temperature FROM temperature")
    result = cursor.fetchall()
    result = [t[0] for t in result]
    return result


X = get_date_time()
Y = get_temperature()

figure = px.line(x=X, y=Y, labels={"x":"Date-Time", "y":"Temperature(C)"})
st.plotly_chart(figure)
