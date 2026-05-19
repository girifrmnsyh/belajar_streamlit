import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='whitegrid')

st.title('Bike Sharing Dashboard')

main_df = pd.read_csv('dashboard/main_data.csv')

st.sidebar.header('Filter')

selected_hour = st.sidebar.slider(
    'Pilih Jam',
    min_value=0,
    max_value=23,
    value=(0,23)
)

filtered_df = main_df[
    (main_df['hr'] >= selected_hour[0]) &
    (main_df['hr'] <= selected_hour[1])
]

st.subheader('Dataset Preview')
st.dataframe(filtered_df.head())

weather_label = {
    1: 'Clear',
    2: 'Mist',
    3: 'Light Snow/Rain',
    4: 'Heavy Rain'
}

filtered_df['weather_label'] = filtered_df['weathersit'].map(weather_label)

st.subheader('Rata-rata Penyewaan Berdasarkan Cuaca')

weather_rentals = (
    filtered_df.groupby('weather_label')['cnt']
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    x=weather_rentals.index,
    y=weather_rentals.values,
    palette='Blues',
    ax=ax
)

ax.set_title('Pengaruh Cuaca terhadap Penyewaan')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Rata-rata Penyewaan')

st.pyplot(fig)

st.subheader('Rata-rata Penyewaan per Jam')

hourly_rentals = filtered_df.groupby('hr')['cnt'].mean()

fig2, ax2 = plt.subplots(figsize=(10,5))