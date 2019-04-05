#Init function for constructor
#all the libraries are imported

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import stats
import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.metrics import accuracy_score as accu
from sklearn.metrics import confusion_matrix as cm
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC, LinearSVC

def __init__():
    print("Successfully Imported gtd_lib")
    data()

def data():
    cwd = os.getcwd()
    os.chdir("gtd_lib")
    df = pd.read_csv('gtd_cleaned.csv', sep=',', index_col=0, engine='python', parse_dates=True, encoding=None,
                     tupleize_cols=None, infer_datetime_format=False)
        # df = df.drop_duplicates().drop(
        #     columns=['iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'provstate', 'city', 'attacktype1_txt',
        #              'targtype1_txt', 'targsubtype1_txt', 'target1', 'natlty1_txt', 'gname', 'weaptype1_txt'])

    os.chdir(cwd)
    return df

__init__()