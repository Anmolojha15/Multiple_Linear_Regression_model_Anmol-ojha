import numpy as np
from flask import Flask, request, jsonify, render_template
#from flask_ngrok import run_with_ngrok
import pickle


app = Flask(__name__)
model = pickle.load(open('house_predict.pkl','rb')) 
#run_with_ngrok(app)

@app.route('/')
def home():
  
    return render_template("model2.html")
  
  
@app.route('/pr',methods=['GET'])
def predict():
  exp1 = float(request.args.get('exp1'))
  exp2 = float(request.args.get('exp2'))
  exp3 = float(request.args.get('exp3'))
  exp4 = float(request.args.get('exp4'))
  exp5 = float(request.args.get('exp5'))
  exp6 = float(request.args.get('exp6'))
  prediction = model.predict([[exp1,exp2,exp3,exp4,exp5,exp6]])
  return render_template('model2.html', prediction_text='Regression Model  has predicted Price for the House : {}'.format(prediction))
if __name__ == "__main__":
  app.run(debug=True)
