import streamlit as st 
import pandas as pd 
import plotly.express as px
st.set_page_config(layout="wide", page_title="Crime Data Analysis")
df = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
st.title("Crime Data Analysis")
st.write(df.head())
col1, col2 = st.columns(2)
with col1:
    st.subheader("Crime Data Overview")
    st.write("Total Records;", df.shape[0])
    st.write("Total Columns:", df.shape[1])
    st.write("Columns Names:", df.columns.tolist())
crime_count=df['Crm Cd Desc'].value_counts().reset_index()
fig=px.bar(crime_count.head(10), x='Crm Cd Desc', y='count',title="Top 10 Crimes")
fig.update_xaxes(tickangle=45)
st.plotly_chart(fig)
st.sidebar.title("Crime Data Analysis and Visualization")
selected_date = st.sidebar.date_input("Selected Date")
selected_area = st.sidebar.multiselect("Select Area", options=df["AREA NAME"].unique())
filtered_area = df[df["AREA NAME"].isin(selected_area)]
selected_crime_type = st.sidebar.multiselect("Select Crime Type", options=df["Crm Cd Desc"].unique()[:29])
st.sidebar.text("Our team Members")
st.sidebar.write("1- Saurabh Pandey")
st.sidebar.write("2- Yuvraj Yadav")

st.sidebar.markdown("--------------------------------------")
st.sidebar.write("College Mini Project")
st.sidebar.write("B.tech Data science Student 3rd Sem ")
st.sidebar.write("Group #6 ")
st.sidebar.write("yuv7474@gmail.com")
st.sidebar.write("Contact: 7307905895")



