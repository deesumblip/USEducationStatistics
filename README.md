# USEducationStatistics
A repository for deploying web apps built using a compilation of US education data. The original dataset (states_all.csv) can be found here: https://www.kaggle.com/noriuk/us-education-datasets-unification-project

The repo includes a zipped development Jupyter notebook that visualises other education metrics of interest.

us_education_app is a preliminary Streamlit app designed to predict Grade 4 reading scores using the above education statistics. Other apps that predict other education metrics using the same dataset are also possible.

The requirements.txt file is required for launching the app through Streamlit. For more information on app deployment, see Streamlit documentation here: https://docs.streamlit.io/en/stable/deploy_streamlit_app.html

The files with .pkl at the end are saved Pickl files generated using PyCaret. These models are then flexibly deployed within the app to create new predictions for reading scores.

Find the app at: https://share.streamlit.io/deesumblip/useducationstatistics/main/us_education_app.py
