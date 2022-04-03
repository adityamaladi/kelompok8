from tkinter import Frame
from nbformat import read
import pandas as pd
# import plotly.express as px
import streamlit as st
import numpy as np
from pandas import DataFrame as df
import pandas as pd

# import DataFrame as df
# import plotly.figure_factory as ff
# import matplotlib.pyplot as plt


# # ---- SIDEBAR ----
# st.sidebar.header("Please Filter Here:")
# city = st.sidebar.multiselect(  # kota
#     "Pilih Kota:",
#     options=df["City"].unique(),
#     default=df["City"].unique()
# )

# customer_type = st.sidebar.multiselect(  # jumlah k
#     "Select the Customer Type:",
#     options=df["Customer_type"].unique(),
#     default=df["Customer_type"].unique(),
# )

# gender = st.sidebar.multiselect(  # jumlah sehat
#     "Select the Gender:",
#     options=df["Gender"].unique(),
#     default=df["Gender"].unique()
# )


# st.set_page_config(page_title="Covid Dashboard")

# df = pd.read_excel(
#     io='covid.xlsx',
#     engine='openpyxl',
#     sheet_name='covid',
#     skiprows=3,
#     usecols="B:R",
#     nrows=1000,

# )

st.header('Dasboard Data Covid 19')
data_covid = pd.read_csv("covidcsv.csv")
st.write(data_covid)
jumlah = data_covid.iloc[:, 7:10]
# total_kasus = jumlah.sum[:, 7, 8, 9, 10]
# total_kasus

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
