import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
from datetime import datetime

import joblib

import json
import csv

# sunifyfuto-default-rtdb-export.json

def prediction():
    
    with open("Sunify_Prediction\sunifyfuto-default-rtdb-export.json", "r", encoding="utf-8") as f:
        dict_ldr = json.load(f)
        timestamp_list = []
        value_list = []
        uniqueid_list = []
        rating_list =[]
        for key, val in dict_ldr["data"].items():
            timestamp_list.append(str(val["timestamp"]))
            value_list.append(val["value"])
            rating_list.append(str(val["rating"]))
            uniqueid_list.append(key)

    sunify_data = pd.DataFrame({"Unique_ID":uniqueid_list, "Date": timestamp_list, "Value":value_list, "Rating": rating_list})
    sunify_data.head()

    df = sunify_data.copy()
    df.Date = df['Date'].astype(str).astype(int)

    date = []
    for elements in df.Date:
        date.append(datetime.utcfromtimestamp(elements).strftime('%Y-%m-%d %H:%M:%S'))

    df["DateTime"] = date
    df.DateTime = pd.to_datetime(df.DateTime)

    df["Year"]= df.DateTime.dt.year
    df["Month"]= df.DateTime.dt.month
    df["Day"]= df.DateTime.dt.day
    df["Hour"]= df.DateTime.dt.hour
    df["Minute"]= df.DateTime.dt.minute
    df["Second"]= df.DateTime.dt.second
    df.head()

    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    df.Rating = encoder.fit_transform(df.Rating)

    #3= very high, 0 = high, 1=low, 2= moderate, 4= very low


    df.drop("Unique_ID", axis =1, inplace=True)
    df.drop("Date", axis =1, inplace=True)


    df.drop("DateTime", axis =1, inplace=True)
    df.head()

    x = df.drop("Rating", axis=1)
    y = df.Rating

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier()
    clf.fit(x_train, y_train)
    clf.score(x_test, y_test)

    clf.predict(x_test)

    # joblib_file = "Predictions.joblib"
    # joblib.dump(clf, joblib_file)

    return(clf.predict(x_test))



