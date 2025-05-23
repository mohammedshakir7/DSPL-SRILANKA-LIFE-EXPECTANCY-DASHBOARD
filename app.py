import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid
import matplotlib.pyplot as plt
import numpy as np  

# Load the dataset
data = pd.read_csv("Cleaned_SriLanka_Data.csv")

# Set up sideebar
st.sidebar.title("Dashboard Sidebar")
st.sidebar.subheader("Select Options")

# Sidebar filters or selection options
chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Chart"], key="chart_type_selectbox")  
min_year = int(data["Year(s)"].min())
max_year = int(data["Year(s)"].max())

selected_year = st.sidebar.slider("Select Year Range", 
                          min_value=min_year, 
                          max_value=max_year, 
                          value=(min_year, max_year), 
                          key="year_slider")

color = st.sidebar.color_picker("Pick a bar color", "#00f900", key="color_picker")

# Main content
st.title("Life Expectancy Visualization")

# Add the discription about the app
st.write("This dashboard visualizes the life expectancy data of Sri Lanka from 1950 to 2100. You can select different years, chart types, and customize the bar color.")

# Display data table
st.write("Displaying the data table:")
AgGrid(data, height=350, fit_columns_on_grid_load=True)

# Filter data based on selected year range
filtered_data = data[(data["Year(s)"] >= selected_year[0]) & (data["Year(s)"] <= selected_year[1])]
st.write(filtered_data)

# Data Visualization Section
st.write("Displaying a bar chart of the Value column:")

# Create a figure and axis for the Matplotlib chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(filtered_data["Year(s)"], filtered_data["Value"])
ax.set_xlabel("Year")
ax.set_ylabel("Value")
ax.set_title("Year vs Value")
st.pyplot(fig)

# Create a Plotly chart with tooltips
fig = px.bar(filtered_data, 
             x="Year(s)", 
             y="Value", 
             hover_data=["Year(s)", "Value"], 
             labels={"Year(s)": "Year", "Value": "Value"}, 
             title="Year vs Value")
st.plotly_chart(fig, key="plotly_chart_1")  

# Create a customized Plotly chart based on selected chart type
if chart_type == "Bar Chart":
    fig = px.bar(filtered_data, 
                 x="Year(s)", 
                 y="Value", 
                 hover_data=["Year(s)", "Value"], 
                 labels={"Year(s)": "Year", "Value": "Value"}, 
                 title="Year vs Value", 
                 color_discrete_sequence=[color])
    st.plotly_chart(fig, key="plotly_chart_2")  
elif chart_type == "Line Chart":
    fig = px.line(filtered_data, 
                  x="Year(s)", 
                  y="Value", 
                  hover_data=["Year(s)", "Value"], 
                  labels={"Year(s)": "Year", "Value": "Value"}, 
                  title="Year vs Value", 
                  color_discrete_sequence=[color])
    st.plotly_chart(fig, key="plotly_chart_3")  

# Footer 
st.markdown("---")
st.markdown("Developed for DSPL Coursework | Mohammed Shakir 2025")
