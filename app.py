from flask import Flask, redirect, url_for, request,render_template
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle 

app = Flask(__name__) 

@app.route('/success/<name>') 
def success(name): 
   return 'welcome %s' % name 
  
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        time = float(request.form['c1'])
        CO_GT = float(request.form['c2'])
        C6h_GT = float(request.form['c3'])
        PT08_S2 = float(request.form['c4'])
        NOx = float(request.form['c5'])
        PT08_S3 = float(request.form['c6'])
        NO2x = float(request.form['c7'])
        PT08_s4 = float(request.form['c8'])
        PT08_s5 = float(request.form['c9'])
        T = float(request.form['c10'])
        AH = float(request.form['c11'])
        ls=[[time,CO_GT,C6h_GT,PT08_S2,NOx,PT08_S3,NO2x,PT08_s4,PT08_s5,T,AH]]
        lm=pickle.load(open('model/Regressor_model.sav','rb'))
        x=lm.predict(ls)
        return 'answer is %f' %x
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
