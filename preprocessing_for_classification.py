# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:37:03 2020

@author: Akash
"""

## Lets import the libraries
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE,RandomOverSampler


file_name = 'pulse.xlsx'
dataframe = pd.read_excel(file_name)
num_rec = dataframe.shape[0]


## Function to fill the NaN values
def fill_na(dataframe):

    for col in dataframe.columns:
        if dataframe[col].dtype.name != 'object':
            if (dataframe[col].isnull().sum())*2 >= num_rec:
                dataframe = dataframe.drop([col], axis=1)
            else:
                dataframe[col] = dataframe[col].fillna(dataframe[col].mean())
    return dataframe


## Function for splitting the dataset        
def splitdata(X,y):
    
    
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
    return X_train, X_test, y_train, y_test

  
## Function for labelencoding
def encode(dataframe):
    
    for col in dataframe.columns:
        if dataframe[col].dtype.name == 'object':
            le = LabelEncoder()
            dataframe[col] = le.fit_transform(dataframe[col])
    return dataframe


## Function for Scaling
def scale(X_train,X_test):
    
    sc = StandardScaler()   
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    return X_train, X_test


## Function for oversampling
def oversample(X,y):
    
    smote = random.choice([SMOTE(),RandomOverSampler()])
    X,y = smote.fit_resample(X,y)
    return X,y

