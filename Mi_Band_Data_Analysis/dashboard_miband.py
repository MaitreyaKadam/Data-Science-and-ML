from collections.abc import Mapping
import streamlit as st
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly import __version__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go
import cufflinks as cf
cf.go_offline()
# Loading the csv file
activity = pd.read_csv("ACTIVITY.csv")
# Outlier Elimination

# load data from CSV file
activity = pd.read_csv('ACTIVITY.csv')

# calculate the interquartile range (IQR) for each feature
Q1 = activity.quantile(0.25)
Q3 = activity.quantile(0.75)
IQR = Q3 - Q1

# identify outliers using the IQR method
outliers = activity[((activity < (Q1 - 1.5 * IQR)) |
                     (activity > (Q3 + 1.5 * IQR))).any(axis=1)]

# remove outliers from the dataset
activity = activity[~((activity < (Q1 - 1.5 * IQR)) |
                      (activity > (Q3 + 1.5 * IQR))).any(axis=1)]

# title for the dashboard
st.markdown("# Fitness Tracker Dashboard")

# defining side bar
st.sidebar.header("Filters:")

# placing filters in the sidebar using unique values.
year = st.sidebar.multiselect(
    "Select Year:",
    options=activity["year"].unique(),

)

# placing filters in the sidebar using unique values.
month_name = st.sidebar.multiselect(
    "Select Month Name:",
    options=activity["month_name"].unique(),

)

# taking the filtered dataframe created in a previous step and applying a query
activity = activity.query("`year` == @year & `month_name` == @month_name")


# defining our metrics
total_steps = activity['steps'].sum()
max_steps = activity['steps'].max()
total_cal = activity['calories'].sum()
high_cal = activity['calories'].max()
total_distance_m=activity['distance'].sum()
total_distance_km = total_distance_m / 1000.0
# placing our metrics within columns in the dashboard
col1, col2, col3, col4,col5 = st.columns(5)
col1.metric(label="Total Steps Taken", value=total_steps)
col2.metric(label='Maximum Steps Taken', value=max_steps)
col3.metric(label="Calories Burned", value=total_cal)
col4.metric(label='Maximum Calories', value=high_cal)
col5.metric(label='Total Distance (km)', value=str(total_distance_km))

# a dividing line
st.divider()
col6, spacer, col7 = st.columns([1, 1.5, 1])
with col6:
    fig_steps = px.pie(activity, values='steps', names='Day', title="Pie Chart of Monthly Steps", color_discrete_sequence=px.colors.sequential.Magma,
                       template="plotly_dark")
    fig_steps.update_traces(textinfo='label+value')
    st.plotly_chart(fig_steps)
with col7:
    fig_calories = px.pie(activity, values='calories', names='Day', title="Pie Chart of Calories Burned", color_discrete_sequence=px.colors.sequential.Magma,
                          template="plotly_dark")
    fig_calories.update_traces(textinfo='label+value')
    st.plotly_chart(fig_calories)


# Plot the first bar chart in the first column
with col6:
    fig_bar_steps = px.bar(activity, x='Day', y='steps', color='steps',
                           title='Monthly Steps Distribution', color_continuous_scale='magma')
    st.plotly_chart(fig_bar_steps)

# Plot the second bar chart in the second column
with col6:
    fig_bar_calories = px.bar(activity, x='Day', y='calories', color='calories',
                              title='Monthly Calories Distribution', color_continuous_scale='magma')
    st.plotly_chart(fig_bar_calories)

st.write("Selected Data:")
st.write(activity)
