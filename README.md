# Thyroid Disease Detection

Around 10% of population in USA and around 50 Million people in India suffer from thyroid disease each year, making it an extremely prevalent issue. The body's metabolism can be sped up or slowed down by a thyroid condition.

The primary goal of this project is to use machine learning to determine if a person has compensated hypothyroidism, primary hypothyroidism, secondary hypothyroidism, or negative (no thyroid). The thyroid dataset from the UCI Machine Learning repository has been used to train classification algorithms like Random Forest, SVM, and KNN Model Using the flask framework, the application has been deployed on Heroku.

# Webpage Link

## For One-User-Input Prediction
Heroku: https://tddoneinput.herokuapp.com/

## For Bulk Prediction
Heroku: https://batchprediction.herokuapp.com/

AWS: http://tddbulkprediction-env.eba-uqgwbduj.us-east-2.elasticbeanstalk.com/

# Technical Aspects

- Python 3.7 and more
- Important Libraries: sklearn, pandas, numpy, matplotlib & seaborn
- Front-end: HTML, CSS 
- Back-end: Flask framework
- IDE: Jupyter Notebook, Pycharm & VSCode
- Database: Cassandra 
- Deployment: Heroku, AWS

# How to run this app 

Code is written in Python 3.7 and more. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.

- Create virtual environment - conda create -n myenv python=3.7
- Activate the environment - conda activate myenv
- Install the packages - pip install -r requirements.txt
- Run the app - python run app.py

# Workflow

## Data Collection

Thyroid Disease Data Set from UCI Machine Learning Repository.

Link:https://archive.ics.uci.edu/ml/datasets/thyroid+disease

## Data Pre-processing

- Missing values handling by Simple imputation (KNN Imputer)
- Outliers detection and removal by boxplot and percentile methods
- Categorical features handling by ordinal encoding and label encoding
- Feature scaling done by Standard Scalar method
- Imbalanced dataset handled by SMOTE
- Drop unnecessary columns

## Model Creation and Evaluation
- Data is divided in clusters 
- Various classification algorithms like Random Forest, SVM, KNN are performed on clusters 
- Each clustes gave best model and that model is saved after hyper parameter tuning
- Model performance evaluated based on accuracy, confusion matrix, classification report.

## Model Deployment
The final model is deployed on Heroku using Flask framework.

## User Interface
### Single User Input Prediction User Interface

## Project Documents

- Architecture: https://github.com/Navanshu04/Thyroid-Disease-Detection/blob/main/Docs/TDD_Architecture_V1.0_2.pdf

- Detailed Project Report: https://github.com/Navanshu04/Thyroid-Disease-Detection/blob/main/Docs/TDD_DPR.pdf

# Author

Navanshu Khare: https://www.linkedin.com/in/navanshu-khare/
