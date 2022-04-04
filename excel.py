from tkinter import Frame
from nbformat import read
import pandas as pd
# import plotly.express as px
import streamlit as st
import numpy as np
from pandas import DataFrame as df

st.header('Dasboard Data Covid 19')
data_covid = pd.read_csv("covidcsv.csv")
st.write(data_covid)
jumlah = data_covid.iloc[:, 7:10]

st.header('Jumlah Kasus Covid-19')
jumlah_kasus = data_covid.iloc[:, 7]
total_kasus = jumlah_kasus.sum()
jumlah_kasus
st.write(total_kasus)

st.header('Jumlah Kasus Mati')
jumlah_mati = data_covid.iloc[:, 8]
total_mati = jumlah_mati.sum()
jumlah_mati
st.write(total_mati)

st.header('Jumlah Kasus Selamat')
jumlah_selamat = data_covid.iloc[:, 9]
total_selamat = jumlah_selamat.sum()
jumlah_selamat
st.write(total_selamat)

st.header('Jumlah Kasus Positif')
jumlah_positif = data_covid.iloc[:, 10]
total_positif = jumlah_positif.sum()
jumlah_positif
st.write(total_positif)
