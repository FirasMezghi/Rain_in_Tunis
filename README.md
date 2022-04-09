# Rain_in_Tunis
Rainy Tunis is a web app which has a Machine Learning model running at the back. The purpose of developing this app is to predict whether it will rain the next day or not in Tunisia. This model is based on dataset that has been web scarped from the website https://fr.tutiempo.net/climat/tunisie.html .

## step1 : Data collection
the data was scraped from the website https://fr.tutiempo.net/climat/tunisie.html .
check out the code https://github.com/FirasMezghi/Rain_in_Tunis/blob/main/Data_collection_rain.ipynb.
the contains several indicators like tempature , pressure , wind velocity... and the weather conditions of the previous day from 2008 to 2021.

## step2: Data cleaning
check out https://github.com/FirasMezghi/Rain_in_Tunis/blob/main/rain_data_cleaning.ipynb

## step3: feature engineering
some of the the features had high correlation coefficient with each other-->removing some features.
check out https://github.com/FirasMezghi/Rain_in_Tunis/blob/main/modeling_rain_.ipynb

## step4: Modeling
after trainning a bunch of models , XGboost had the best score.
check out https://github.com/FirasMezghi/Rain_in_Tunis/blob/main/modeling_rain_.ipynb

##step4: deployment:
I used flask to web app where i deployed the model.
check out the demo video 


