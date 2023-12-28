import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Baca data dari file
df = pd.read_csv("https://raw.githubusercontent.com/liyue-com/bike-sharing-dataset/ded2825e2fb66e6dd8210ac4abb4b364562fd037/Proyek%20Analisis%20data/clean_bikeshare_hour.csv")

# Tampilkan data
st.write("Data yang dibaca:")
st.write(df)

# Menghitung total per musim
seasonly_users_df = df.groupby("season").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
}).reset_index()

# Menentukan urutan musim
season_order = ['Spring', 'Summer', 'Fall', 'Winter']

# Membuat bar chart dengan Plotly Express
fig_season = px.bar(
    seasonly_users_df,
    x="season",
    y="cnt",
    title="Count of bikeshare rides by Season",
    labels={"cnt": "Total Rides", "season": "Season"},
    category_orders={"season": season_order},
)

# Menampilkan grafik musiman menggunakan Streamlit dan Plotly Express
st.plotly_chart(fig_season)

# Menampilkan judul untuk grafik berikutnya
st.title("Monthly count of bikeshare rides (2011-2012)")

# Pilihan untuk menampilkan grafik
show_plot = st.checkbox("Show Plot", value=True)

if show_plot:
    # Mengganti ukuran plot
    plt.figure(figsize=(16, 6))

    # Membuat plot menggunakan seaborn
    sns.lineplot(x="dteday", y="cnt", data=df, color='blue')

    # Menambahkan label dan judul
    plt.xlabel("Date")
    plt.ylabel("Total Rides")

    # Menampilkan plot di Streamlit
    st.pyplot(plt)

    # Menampilkan informasi tambahan di bawah plot jika diperlukan
    st.info("Monthly count of bikeshare rides (2011-2012)")
