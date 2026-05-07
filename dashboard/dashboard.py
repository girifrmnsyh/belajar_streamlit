import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# konfigurasi style
sns.set(style='whitegrid')

# title dashboard
st.title("Bike Sharing Dashboard")

# load data
main_df = pd.read_csv("dashboard/main_data.csv")

# tampilkan data
st.subheader("Dataset Preview")
st.dataframe(main_df.head())

# mapping label cuaca
weather_label = {
    1: "Clear",
    2: "Mist",
    3: "Light Snow/Rain",
    4: "Heavy Rain"
}

main_df["weather_label"] = main_df["weathersit"].map(weather_label)

# ======================
# VISUALISASI 1
# ======================

st.subheader("Rata-rata Penyewaan Berdasarkan Cuaca")

weather_rentals = (
    main_df.groupby("weather_label")["cnt"]
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    x=weather_rentals.index,
    y=weather_rentals.values,
    palette="Blues",
    ax=ax
)

ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_title("Pengaruh Cuaca terhadap Penyewaan")

st.pyplot(fig)

# ======================
# VISUALISASI 2
# ======================

st.subheader("Rata-rata Penyewaan per Jam")

hourly_rentals = main_df.groupby("hr")["cnt"].mean()

fig2, ax2 = plt.subplots(figsize=(10,5))

sns.lineplot(
    x=hourly_rentals.index,
    y=hourly_rentals.values,
    marker="o",
    ax=ax2
)

ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Penyewaan")
ax2.set_title("Pola Penyewaan Sepeda per Jam")

st.pyplot(fig2)

# ======================
# KESIMPULAN
# ======================

st.subheader("Insight")

st.write("""
1. Cuaca cerah menghasilkan jumlah penyewaan sepeda tertinggi.

2. Penyewaan sepeda meningkat pada jam sibuk,
terutama pagi dan sore hari.
""")