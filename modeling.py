import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.model_selection import train_test_split
import sklearn.preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings("ignore")

from scipy import stats
import re

#import acquire
import prepare as p


def model_prep(train, validate, test):
    #features to keep
    keep_columns = ['volatile acidity','citric acid','fixed acidity','sulphates', 'alcohol', 'free sulfur dioxide', 'is_viable'] 
    train = train[keep_columns]
    validate = validate[keep_columns]
    test = test[keep_columns]
    
    train_x = train.drop(columns='is_viable').reset_index(drop=True)
    train_y = train[['is_viable']].reset_index(drop=True)

    validate_x = validate.drop(columns='is_viable').reset_index(drop=True)
    validate_y = validate[['is_viable']].reset_index(drop=True)

    test_x = test.drop(columns='is_viable').reset_index(drop=True)
    test_y = test[['is_viable']].reset_index(drop=True)
    
    return train_x, validate_x, test_x, train_y, validate_y, test_y

def get_tree(train_x, validate_x, train_y, validate_y):
    
    '''get decision tree accuracy on train and validate'''
    #create classifier then fit
    tree = DecisionTreeClassifier(max_depth=4, random_state=123)
    tree = tree.fit(train_x, train_y)

    print(f"Accuracy of Decision Tree on train data is {tree.score(train_x, train_y)}")
    print(f"Accuracy of Decision Tree on validate data is {tree.score(validate_x, validate_y)}")
    


def get_rf(train_x, validate_x, train_y, validate_y):

    '''get rf accuracy on train and validate'''
    #create classifier and fit
    rf = RandomForestClassifier(max_depth=4, random_state=123)
    rf = rf.fit(train_x, train_y)

    print(f"Accuracy of Random Forest on train data is {rf.score(train_x, train_y)}")
    print(f"Accuracy of Random Forest on validate data is {rf.score(validate_x, validate_y)}")


def get_reg(train_x, validate_x, train_y, validate_y):

    '''get reg accuracy on train and validate'''
    #create classifier and fit
    logit = LogisticRegression(solver='liblinear')
    logit = logit.fit(train_x, train_y)

    print(f"Accuracy of Logistic Regression on train is {logit.score(train_x, train_y)}")
    print(f"Accuracy of Logistic Regression on validate is {logit.score(validate_x, validate_y)}")



def get_knn(train_x, validate_x, train_y, validate_y):
    
    '''get knn accuracy on train and validate'''
    knn = KNeighborsClassifier(n_neighbors=7, weights='uniform')
    knn = knn.fit(train_x, train_y)

    # print results
    print(f"Accuracy of KNN on train is {knn.score(train_x, train_y)}")
    print(f"Accuracy of KNN on validate is {knn.score(validate_x, validate_y)}")


def get_rf_test(train_x, test_x, train_y, test_y):

    '''get rf accuracy on train and test'''
    #create classifier and fit
    rf = RandomForestClassifier(max_depth=4, random_state=123)
    rf = rf.fit(train_x, train_y)

    print(f"Accuracy of Random Forest on train data is {rf.score(train_x, train_y)}")
    print(f"Accuracy of Random Forest on test data is {rf.score(test_x, test_y)}")

