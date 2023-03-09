from flask import Flask,request,jsonify
from keras.preprocessing.sequence import TimeseriesGenerator
# from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

@app.route('/api',methods=['GET'])

def hello_world():

	import pandas as pd
	import numpy as np  # linear algebra
	import tensorflow as tf
	from tensorflow.keras.layers import Bidirectional
	import yfinance as yf
	from keras.preprocessing.sequence import TimeseriesGenerator
	from keras.models import load_model
	import numpy as np
	import pandas as pd
	import tensorflow as tf
	import matplotlib as mpl
	import matplotlib.pyplot as plt
	import pandas as pd

	from sklearn.model_selection import train_test_split
	from keras.preprocessing.sequence import TimeseriesGenerator
	from sklearn.preprocessing import MinMaxScaler, StandardScaler
	from sklearn.metrics import accuracy_score
	from cytoolz import sliding_window
	import numpy as np  # linear algebra
	import pandas as pd


	# # ----- รับข้อมูลจากหน้า web ---------
	# d = {}
	# d['Soybean_meal_US'] = float(request.args['Soybean_meal_US'])
	# d['Crude_Oil'] = float(request.args['Crude_Oil'])
	# d['New_Month'] = float(request.args['New_Month'])
	# d['Year'] = float(request.args['Year'])
	#
	# df_input = pd.DataFrame([d]) #แปลงเป็น dataframe
	# # print(df_input.dtypes)
	# # d['Soybean_meal_US'] = d['Soybean_meal_US'].astype(float)
	# year = int(d['Year'])
	# month = int(d['New_Month'])
	# print('month')
	# print(month)
	# # print(type(d))

	# # --------print เช็ค และแปลงวันเดือนปีเอาไว้ดึง yahoo finance ------
	# month_user = month
	# year_user = year - 543
	# year_diff = year - 543
	#
	# new_month = month_user
	# for i in range(3):
	# 	if (month_user > 1):
	# 		month_user = month_user - 1
	# 	else:
	# 		month_user = 12
	# 		year_diff = year_user - 1
	#
	# year_user = str(year_user)
	# year_diff = str(year_diff)
	# end_date = year_user + "-" + str(new_month) + "-01"
	# start_date = year_diff + "-" + str(month_user) + "-01"
	# print(end_date)
	# print(start_date)

	# #------- ดึงข้อมูลจาก Yahoo! finance ราคาน้ำมันกับถั้วเหลือง ---------
	#
	# data_crude_oil = yf.download(tickers="CL=F", start=start_date, end=end_date, interval='1mo')
	# data_crude_oil = data_crude_oil['Close']
	# data_soybean_meal = yf.download(tickers="ZM=F", start=start_date, end=end_date, interval='1mo')
	# data_soybean_meal = data_soybean_meal['Close']
	# # เตรียม data ให้อยู่ในรูปแบบที่จะไปใช้ทำนาย
	# user_input = [[end_date, month, year-543, d['Crude_Oil'], d['Soybean_meal_US']]]

	df = pd.read_excel('dataofPrice_Train.xlsx')
	print(df)

	return jsonify(1)

if __name__ == '__main__':
	app.run(debug=False)