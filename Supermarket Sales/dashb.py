import streamlit as st
import pandas as pd
import plotly_express as px

# Com uma visão mensal;
# Faturamento por unidade;
# Tipo de produto mais vendido, contribuição por filial;
# Desempenho das formas de pagamentos;
# Como estão as avaliações das filiais

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtred = df[df["Month"] ==month]

col1 , col2 = st.columns(2)
col3 , col4, col5 = st.columns(3)

fig_date = px.bar(df_filtred, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)


fig_prod = px.bar(df_filtred, x="Date", y="Product line", 
                  color="City", title="Faturamento por tipo de produto",
                  orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)


city_total = df_filtred.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city)

fig_kind = px.pie(df_filtred, values="Total", names="Payment", 
                  title="Faturamento por filial")
col4.plotly_chart(fig_kind, use_container_width=True)


city_total = df_filtred.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(city_total, x="City", y="Rating", title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)
