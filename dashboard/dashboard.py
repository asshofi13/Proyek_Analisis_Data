from seaborn._core.data import PlotData
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("day.csv")
df = pd.read_csv("hour.csv")

st.title("Proyek Analisis Data")
st.sidebar.header("Bike Sharing")
st.subheader("Visualisasi Data")

st.write("Jumlah Pengguna Kasual Berdasarkan Musim")
casual_season = df.groupby('season')['casual'].sum()
st.bar_chart(casual_season)

st.write("Performa Pengguna Kasual dan Pengguna Terdaftar")
plt.figure(figsize=(24, 5))
monthly_counts = df['casual'].groupby(df['dteday']).max()
plt.scatter(monthly_counts.index, monthly_counts.values, c="#72BCD4", s=10, marker='o')
plt.plot(monthly_counts.index, monthly_counts.values)
plt.xlabel('Bulan')
plt.ylabel('Jumlah')
plt.title('Grafik Jumlah Pengguna kasual per Bulan pada Tahun 2011-2012')
st.pyplot(plt)

plt.figure(figsize=(24, 5))
monthly_counts = df['registered'].groupby(df['dteday']).max()
plt.scatter(monthly_counts.index, monthly_counts.values, c="#72BCD4", s=10, marker='o')
plt.plot(monthly_counts.index, monthly_counts.values)
plt.xlabel('Bulan')
plt.ylabel('Jumlah')
plt.title('Grafik Jumlah Pengguna Terdaftar per Bulan pada Tahun 2011-2012')
plt.legend()
st.pyplot(plt)

st.write("Waktu Paling Banyak Jumlah Pengguna Terdaftar Menyewa Sepeda")
sum_order_items_df = df.groupby("hr").registered.sum().sort_values(ascending=False).reset_index()
fig, ax = plt.subplots(figsize=(35, 15))
sns.barplot(x="hr", y="registered", data=sum_order_items_df.head(5), palette=["#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3"], ax=ax)
ax.set_ylabel(None)
ax.set_xlabel("Hours (PM)", fontsize=20)
ax.set_title("Jam dengan banyak pengguna terdaftar menyewa sepeda", loc="center", fontsize=30)
ax.tick_params(axis='y', labelsize=15)
ax.tick_params(axis='x', labelsize=15)
plt.legend()
st.pyplot(plt)

st.caption('Copyright © Dicoding 2023')