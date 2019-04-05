import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.metrics import accuracy_score as accu
from sklearn.metrics import confusion_matrix as cm
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC, LinearSVC

def __init__(data):
    df = data.drop_duplicates().drop(columns = ['iyear','imonth','iday','country_txt','region_txt','provstate','city','attacktype1_txt','targtype1_txt','targsubtype1_txt','target1','natlty1_txt','gname','weaptype1_txt'])
    df = df.dropna()
    return df

def predict_nb(df):
    df = __init__(df)
    X_train, X_test = train_test_split(df, test_size=0.7, random_state=int(time.time()))
    gnb = GaussianNB()
    gnb.fit(X_train.values, X_train['gname_num'])
    y_pred = gnb.predict(X_test)
    accuracy =accu(X_test['gname_num'], y_pred)
    print(accuracy)

# def predict_svm(df):
#     df = __init__(df)
#     X_train, X_test = train_test_split(df, test_size=0.7, random_state=int(time.time()))
#     svm =SGDClassifier()
#     svm.fit(X_train.values,X_train['gname_num'])
#     y_pred = svm.predict(X_test)
#     accu(X_test['gname_num'],y_pred)
