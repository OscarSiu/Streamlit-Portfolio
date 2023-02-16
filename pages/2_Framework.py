import streamlit as st
import pandas as pd

siteHeader = st.container()
dataExploration = st.container()
newFeatures = st.container()
modelTraining = st.container()

with siteHeader:
    st.title('Welcome to the Awesome project!')
    st.text('In this project I look into ... And I try ... I worked with the dataset from ...')

with dataExploration:
    st.header('Dataset: Iris flower dataset')
    st.text('I found this dataset at... I decided to work with it because ...')
    #taxi_data = pd.read_csv('data/taxi_data.csv')  #2
    #distribution_pickup = pd.DataFrame(taxi_data['PULocationID'].value_counts())   #3
    #st.bar_chart(distribution_pickup)    #4


with newFeatures:
    st.header('New features I came up with')
    st.text('Let\'s take a look into the features I generated.')
    st.markdown('* **first feature:** this is the explanation')
    st.markdown('* **second feature:** another explanation')

with modelTraining:
    st.header('Model training')
    st.text('In this section you can select the hyperparameters!')