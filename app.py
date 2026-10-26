import streamlit as st 
import pandas as pd 
import plotly.express as px
st.set_page_config(layout="wide", page_title="Crime Data Analysis")
df = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
st.title("Crime Data Analysis & Visualisation")
st.write("State and district crime trends from NCRB data with hotspot maps")
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
st.subheader("OVERVIEW")
st.write(
    """
--> This dashboard provides a detailed and interactive analysis of crime cases and their trends across different regions. 
By utilizing data from the National Crime Records Bureau (NCRB), the application illustrates the distribution of various types of crimes. 
Through this, users can observe which crimes are reported in the highest numbers and which areas are most affected. 
The visualization of data helps in identifying hotspots, allowing for better security measures and resource allocation. 
This project presents a practical approach to navigating the complexities of real-world data analysis and assisting in decision-making.
"""
)
st.subheader("Methodology")
st.write(
    """
This project involves collecting crime data, cleaning and pre-processing it for analysis. 
We used libraries like Pandas for data manipulation and Plotly Express for creating interactive visualizations, ensuring the data is easily interpretable.
"""
)
st.subheader("Future Scope")
st.write(
    """
Future enhancements could include integrating real-time crime data updates, deploying predictive machine learning models to forecast crime patterns, and adding advanced geospatial analysis to improve emergency response times.
"""
)
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
st.sidebar.write("Contact: 7307905895,9569133345")



