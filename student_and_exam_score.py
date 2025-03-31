import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

modle = LinearRegression()
studyhour = {'Studu_Hour':[1,2,3,4,5,6,7,8,9,10],'Exam_Score':[50,55,60,65,70,75,80,85,90,50]}

df = pd.DataFrame(studyhour)
#print(df)

X = df[['Studu_Hour']]

y = df[['Exam_Score']]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

modle.fit(X_train, y_train)

user_input_testing = float(input("Enter the numers of you study: "))

prediced = modle.predict([[user_input_testing]])

print(f"Predicted exam score: {prediced[0][0]:.2f}")