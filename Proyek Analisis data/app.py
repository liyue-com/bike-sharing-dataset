import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("/content/clean_bikeshare_hour.csv")


st.write("Data yang dibaca:")
st.write(df)


seasonly_users_df = df.groupby("season").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
}).reset_index()


season_order = ['Spring', 'Summer', 'Fall', 'Winter']


fig_season = px.bar(
    seasonly_users_df,
    x="season",
    y="cnt",
    title="Count of bikeshare rides by Season",
    labels={"cnt": "Total Rides", "season": "Season"},
    category_orders={"season": season_order},
)

st.plotly_chart(fig_season)

st.title("Monthly count of bikeshare rides (2011-2012)")


show_plot = st.checkbox("Show Plot", value=True)

if show_plot:
  
    plt.figure(figsize=(16, 6))

 
    sns.lineplot(x="dteday", y="cnt", data=df, color='blue')

   
    plt.xlabel("Date")
    plt.ylabel("Total Rides")

    st.pyplot(plt)


    st.info("Monthly count of bikeshare rides (2011-2012)")
