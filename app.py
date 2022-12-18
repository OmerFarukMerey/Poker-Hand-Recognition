import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
import pickle

import warnings
warnings.filterwarnings('ignore')
st.write('Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}')
st.write('Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)')
st.write('Please give your outputs based on the notation above.')
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

def add_unique_count(df):
    tmp_suit = df[["S1", "S2", "S3", "S4", "S5"]]
    df["unique_suit"] = tmp_suit.apply(lambda s: len(np.unique(s)), axis=1)
    return df

suit1 = st.select_slider(
    'Select a Suit of the Card 1 (Ordinal Value: 1,2,3 or 4)',
    options=[1, 2, 3, 4])
st.write('Suit of the Card 1 is', suit1)

rank1 = st.select_slider(
    'Select a Rank of the Card 1 (Ordinal Value: 1,2,3,4,5,6,7,8,9,10,11,12,13)',
    options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
st.write('Suit of the Card 1 is', rank1)

suit2 = st.select_slider(
    'Select a Suit of the Card 2 (Ordinal Value: 1,2,3 or 4)',
    options=[1, 2, 3, 4])
st.write('Suit of the Card 2 is', suit2)

rank2 = st.select_slider(
    'Select a Rank of the Card 2 (Ordinal Value: 1,2,3,4,5,6,7,8,9,10,11,12,13)',
    options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
st.write('Suit of the Card 2 is', rank2)

suit3 = st.select_slider(
    'Select a Suit of the Card 3 (Ordinal Value: 1,2,3 or 4)',
    options=[1, 2, 3, 4])
st.write('Suit of the Card 3 is', suit3)

rank3 = st.select_slider(
    'Select a Rank of the Card 3 (Ordinal Value: 1,2,3,4,5,6,7,8,9,10,11,12,13)',
    options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
st.write('Suit of the Card 3 is', rank3)

suit4 = st.select_slider(
    'Select a Suit of the Card 4 (Ordinal Value: 1,2,3 or 4)',
    options=[1, 2, 3, 4])
st.write('Suit of the Card 4 is', suit4)

rank4 = st.select_slider(
    'Select a Rank of the Card 4 (Ordinal Value: 1,2,3,4,5,6,7,8,9,10,11,12,13)',
    options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
st.write('Suit of the Card 4 is', rank4)

suit5 = st.select_slider(
    'Select a Suit of the Card 5 (Ordinal Value: 1,2,3 or 4)',
    options=[1, 2, 3, 4])
st.write('Suit of the Card 5 is', suit5)

rank5 = st.select_slider(
    'Select a Rank of the Card 5 (Ordinal Value: 1,2,3,4,5,6,7,8,9,10,11,12,13)',
    options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
st.write('Suit of the Card 5 is', rank5)

nn_model = pickle.load(open('nn_model.pickle', 'rb'))

data = {
    'S1':suit1,
    'C1':rank1,
    'S2':suit2,
    'C2':rank2,
    'S3':suit3,
    'C3':rank3,
    'S4':suit4,
    'C4':rank4,
    'S5':suit5,
    'C5':rank5
}
df = pd.DataFrame(data, index=[0])
df = preprocess_data(df)

res = nn_model.predict(df)

rank_name = {
    '0': 'No pairs',
    '1': 'One pair',
    '2': 'Two pairs',
    '3': 'Three of a kind',
    '4': 'Straight',
    '5': 'Flush',
    '6': 'Full house',
    '7': 'Four of a kind',
    '8': 'Straight flush',
    '9': 'Royal flush',
}


st.write('The result is:', res[0], ' and your hand is ', rank_name[str(res[0])],'!')


st.write("""
# Poker Hand Recognition App
This app predicts the Poker
""")
