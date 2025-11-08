import os

import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#set page config
st.set_page_config(page_title="Data Visualizer", layout= "centered")

#set page title
st.title("📈 Data Visualizer App 📊")

#get working directory
working_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = f"{working_dir}/data"

files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

#Dropdown all the files
selected_file = st.selectbox("Select a file", files_list, index = None)

if selected_file:

    #get the file path
    file_path = os.path.join(folder_path, selected_file)

    #read the csv file
    df = pd.read_csv(file_path)

    #get the columns names of the csv file
    cols = df.columns.to_list()

    #print the fisrt 5 rows, for displaying only
    st.write("")
    st.write(df.head())

    #select the columns
    x_axis = st.selectbox("Select the X-axis", cols + ["None"], index = None)
    y_axis = st.selectbox("Select the Y-axis", cols + ["None"], index = None)

    plot_list = ["Bar Chart", "Distribution Plot", "Scatter Plot"]

    selected_plot = st.selectbox("Select the Plot", plot_list)
    
#button to generate the plot
if st.button("Generate Plot"):
    fig, ax = plt.subplots(figsize = (6,4))

    if selected_plot == "Bar Chart":
        sns.barplot(x = df[x_axis], y = df[y_axis], ax = ax)
    
    elif selected_plot == "Distribution Plot":
        sns.histplot(x = df[x_axis], kde = True, ax = ax)
    
    elif selected_plot == "Scatter Plot":
        sns.scatterplot(x = df[x_axis], y = df[y_axis], ax = ax)

    #adjust label size
    ax.tick_params(axis = "x", labelsize = 10)
    ax.tick_params(axis = "y", labelsize = 10)

    #title axis labels
    plt.title(f"{selected_plot} of {y_axis} vs {x_axis}", fontsize = 12)
    plt.xlabel(x_axis, fontsize = 10)
    plt.ylabel(y_axis, fontsize = 10)

    st.pyplot(fig)