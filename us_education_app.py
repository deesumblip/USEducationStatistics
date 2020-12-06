# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:13:28 2020

@author: Dilini
"""
from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def run():
    st.sidebar.title("Machine Learning Model Selector")
    add_model_selectbox = st.sidebar.selectbox(
        "Pick a prediction model",
        ("Linear Regression", "Huber Regression", "Bayesian Ridge", "Blended Model"))

    if add_model_selectbox == "Linear Regression":
        model = load_model('Final_LR_Model_05_Dec2020')
    elif add_model_selectbox == "Huber Regression":
        model = load_model('Final_huber_Model_05Dec2020')
    elif add_model_selectbox == "Bayesian Ridge":
        model = load_model('Final_br_Model_05Dec2020')
    elif add_model_selectbox == "Blended Model":
        model = load_model('Final_top3_Model_05Dec2020')

    def predict(model, input_df):
        predictions_df = predict_model(estimator=model, data=input_df)
        predictions = predictions_df['Label'][0]
        return predictions


    st.sidebar.success('This app was developed using the following compilation of US education data: https://www.kaggle.com/noriuk/us-education-datasets-unification-project') # CHANGE LATER
    
    st.title("Explore US Education Data")
    st.markdown('Select a model from the sidebar dropdown menu to generate a prediction for Grade 4 Reading Score below. This app can be used to explore the relationship between various measures of revenue and expenditure and levels of reading score attainment.')

    st.info('Move the sliders and click Predict to generate a Reading Score prediction')
    STATE = st.text_input("Enter ONE full state name, example ARIZONA, CALIFORINIA, WYOMING, etc.")
    YEAR = st.slider('Year', 1986, 2020, 1995, 1)
    ENROLL = st.slider('Enter the number of students enrolled', 0, 1000000, 500000, 100)
    FEDERAL_REVENUE = st.slider('Enter the amount of Federal Revenue received', 0, 11000000, 5500000, 100)
    STATE_REVENUE = st.slider('Enter the amount of State revenue received', 0, 11000000, 5500000, 100)
    LOCAL_REVENUE = st.slider('Enter the amount of Local revenue received', 0, 11000000, 5500000, 100)
    INSTRUCTION_EXPENDITURE = st.slider('Enter the amount of expenses in instruction', 0, 11000000, 5500000, 100)
    SUPPORT_SERVICES_EXPENDITURE = st.slider("Enter the amount of Support Services expenditure", 0, 11000000, 5500000, 100)
    OTHER_EXPENDITURE = st.slider("Enter the amount of expenditure classed as 'Other'", 0, 11000000, 5500000, 100)
    CAPITAL_OUTLAY_EXPENDITURE = st.slider("Enter the amount of Capital Outlay expenditure", 0, 11000000, 5500000, 100)

    output=""

    input_dict = {'STATE' : STATE,
                  'YEAR' : YEAR,
                  'ENROLL' : ENROLL,
                  'FEDERAL_REVENUE' : FEDERAL_REVENUE,
                  'STATE_REVENUE' : STATE_REVENUE,
                  'LOCAL_REVENUE' : LOCAL_REVENUE,
                  'INSTRUCTION_EXPENDITURE': INSTRUCTION_EXPENDITURE,
                  'SUPPORT_SERVICES_EXPENDITURE': SUPPORT_SERVICES_EXPENDITURE,
                  'OTHER_EXPENDITURE': OTHER_EXPENDITURE,
                  'CAPITAL_OUTLAY_EXPENDITURE': CAPITAL_OUTLAY_EXPENDITURE}
    input_df = pd.DataFrame([input_dict])


    if st.button("Predict"):
        output = predict(model=model, input_df=input_df)
        output = str(output)

    st.success('Predicted Grade 4 reading score: {}'.format(output))

if __name__ == '__main__':
    run()

