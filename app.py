from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import datetime
import pickle



app = Flask(__name__, template_folder="templates")
model = pickle.load(open("./model_xg.pkl", "rb"))
print("Model Loaded")

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
	if request.method == "POST":
		
		date = request.form['date']
		year = float(pd.to_datetime(date, format="%Y-%m-%dT").year)
		month = float(pd.to_datetime(date, format="%Y-%m-%dT").month)
		
		TM = float(request.form['maxtemp'])
		
		PP = float(request.form['precipitation'])
		
		VM = float(request.form['windmaxspeed'])
		H = float(request.form['humidity'])
		VV = float(request.form['visibilty'])
		
		RA = int(request.form['raintoday'])
		SN = int(request.form['snowtoday'])
		TS = int(request.form['stormtoday'])
		FG = int(request.form['fogtoday'])

		input_lst = pd.DataFrame({'TM':[TM],'H':[H],'PP':[PP],'VV':[VV],'VM':[VV],'RA':[RA],'SN':[SN],'TS':[TS],'FG':[FG],'month':[month],'year':[year]})
		pred = model.predict(input_lst)
		output = pred
		if output[0] == 0:
			return render_template("sunny.html")
		else:
			return render_template("rainy.html")
	return render_template("prediction.html")
if __name__=='__main__':
	app.run(debug=True)