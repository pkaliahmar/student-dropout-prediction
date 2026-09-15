# 🎓 Student Dropout Prediction

## Overview

This project uses Machine Learning to predict whether a student may be at risk of dropping out.

A Logistic Regression model was trained using student academic, demographic, socioeconomic, and enrollment-related information.

The project demonstrates a complete Machine Learning workflow from data preprocessing to deployment.

## Problem Statement

Student dropout is an important challenge for educational institutions.

The objective of this project is to identify students who may be at risk of dropping out so that institutions can provide early support and intervention.

## Dataset

The dataset contains:

- 4,424 student records
- 37 original columns
- Academic information
- Demographic information
- Socioeconomic information
- Enrollment-related information

The original target contained:

- Graduate
- Dropout
- Enrolled

For this project, the target was converted into binary classification:

- 1 = Dropout / At Risk
- 0 = Not Dropout

## Data Preprocessing

The following steps were performed:

- Missing-value analysis
- Duplicate-value analysis
- Target transformation
- One-hot encoding
- Boolean-to-integer conversion
- Feature preparation

After encoding, the dataset contained 238 input features.

## Exploratory Data Analysis

The project investigated relationships between:

- Academic performance
- Student outcomes
- Scholarship status
- Tuition status
- Other student characteristics

Visualizations were created to understand patterns associated with dropout outcomes.

## Machine Learning Model

### Logistic Regression

Logistic Regression was selected because the project is a binary classification problem.

The dataset was split into:

- 80% training data
- 20% testing data

## Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

## Prediction Application

A Streamlit application allows users to enter student information and receive:

- Dropout probability
- Dropout prediction
- Risk category

Risk categories:

- Low Risk
- Medium Risk
- High Risk

## Educational Early-Warning System

The project could potentially support educational institutions by identifying students who may require additional assistance.

Possible interventions could include:

- Academic counseling
- Financial support
- Tutoring
- Student services
- Personalized intervention

The model should be treated as a decision-support tool and not as a definitive judgment about a student's future.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Logistic Regression
- Streamlit
- Google Colab
- GitHub

## Project Workflow

Dataset  
↓  
Data Cleaning  
↓  
Preprocessing  
↓  
Exploratory Data Analysis  
↓  
Train/Test Split  
↓  
Logistic Regression  
↓  
Model Evaluation  
↓  
Prediction  
↓  
Streamlit Deployment
