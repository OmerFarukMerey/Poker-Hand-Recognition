# Importing necessary modules
from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

# Loading the Models
model = pickle.load(open('model.pkl', 'rb'))

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

 pred = model.predict(arr)
 return render_template('output.html', data=pred)
# Flask server
if __name__=="__main__":
 app.run(debug=True)