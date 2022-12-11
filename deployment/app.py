# Importing necessary modules
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from catboost import Pool

def add_counts(df):
    tmp_card = df[["C1", "C2", "C3", "C4", "C5"]]
    tmp_suit = df[["S1", "S2", "S3", "S4", "S5"]]
    #Pairs, sets, and quads. (equal ranks)
    df["cnt_c1"] = tmp_card.apply(lambda c: sum(c==c[0]), axis=1)
    df["cnt_c2"] = tmp_card.apply(lambda c: sum(c==c[1]), axis=1)
    df["cnt_c3"] = tmp_card.apply(lambda c: sum(c==c[2]), axis=1)
    df["cnt_c4"] = tmp_card.apply(lambda c: sum(c==c[3]), axis=1)
    df["cnt_c5"] = tmp_card.apply(lambda c: sum(c==c[4]), axis=1)
    # Flushes (five cards with the same suit)
    df["cnt_s1"] = tmp_suit.apply(lambda s: sum(s==s[0]), axis=1)
    df["cnt_s2"] = tmp_suit.apply(lambda s: sum(s==s[1]), axis=1)
    df["cnt_s3"] = tmp_suit.apply(lambda s: sum(s==s[2]), axis=1)
    df["cnt_s4"] = tmp_suit.apply(lambda s: sum(s==s[3]), axis=1)
    df["cnt_s5"] = tmp_suit.apply(lambda s: sum(s==s[4]), axis=1)
    return df

def add_unique_count(df):
    tmp_suit = df[["S1", "S2", "S3", "S4", "S5"]]
    df["unique_suit"] = tmp_suit.apply(lambda s: len(np.unique(s)), axis=1)
    return df

def add_diffs(df):
    tmp = df
    #if a straight is possible
    df["diff_1"] = tmp["C2"] - tmp["C1"]
    df["diff_2"] = tmp["C3"] - tmp["C2"]
    df["diff_3"] = tmp["C4"] - tmp["C3"]
    df["diff_4"] = tmp["C5"] - tmp["C4"]
    #Counts how many similar differences there are
    tmp_diff = df[["diff_1","diff_2","diff_3","diff_4"]]
    df["cnt_diff1"] = tmp_diff.apply(lambda c: sum(c==c[0]), axis=1)
    df["cnt_diff2"] = tmp_diff.apply(lambda c: sum(c==c[1]), axis=1)
    df["cnt_diff3"] = tmp_diff.apply(lambda c: sum(c==c[2]), axis=1)
    df["cnt_diff4"] = tmp_diff.apply(lambda c: sum(c==c[3]), axis=1)
    return df

def preprocess_data(data):
    df = data.copy()
    cards = df[["C1", "C2", "C3", "C4", "C5"]]
    suits = df[["S1", "S2", "S3", "S4", "S5"]]
    cards.values.sort()
    suits.values.sort()
    df[["C1", "C2", "C3", "C4", "C5"]] = cards
    df[["S1", "S2", "S3", "S4", "S5"]] = suits
    df = df[["S1", "C1","S2", "C2","S3", "C3","S4", "C4","S5", "C5"]]
    df = add_counts(df)
    df = add_diffs(df)
    df = add_unique_count(df)
    return df

# Loading the Models
model = pickle.load(open('cat_boost.pkl', 'rb'))

# Instantiate app object 
app = Flask(__name__)
# Setting up app routes
@app.route('/')
def man(): 
 return render_template('home.html')
@app.route('/predict', methods=['POST'])
def home():
 feature1 = int(request.form['a'])
 feature2 = int(request.form['b'])
 feature3 = int(request.form['c'])
 feature4 = int(request.form['d'])
 feature5 = int(request.form['e'])
 feature6 = int(request.form['f'])
 feature7 = int(request.form['g'])
 feature8 = int(request.form['h'])
 feature9 = int(request.form['i'])
 feature10 = int(request.form['j'])
 arr = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10]])
 df = pd.DataFrame(arr, columns = ["S1", "C1", "S2", "C2", "S3", "C3", "S4", "C4", "S5", "C5"])
 df = preprocess_data(df)

 pred = model.predict(arr)
 return render_template('output.html', data=pred)
# Flask server
if __name__=="__main__":
 app.run(debug=True)