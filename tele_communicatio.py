import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

data = {'Age':[20,25,30,35,40,55,32,28],
       'Charge':[45,50,80,40,100,120,70,55],
       'Chunk':[0,1,0,1,0,1,0,1]}

df = pd.DataFrame(data)
#print(df)

x_ = df[['Age', 'Charge']]
y = df['Chunk']

x_train, x_test, y_train, y_test = train_test_split(x_, y, test_size = 0.2, random_state=42)

svc_modle = SVC(kernel = 'linear', C = 1.0)

svc_modle.fit(x_train, y_train)

y_pred = svc_modle.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(report)

user_age = float(input("Enter User Age: "))
user_monthly_charge = float(input("Enter User Charge: "))

user_input = np.array([[user_age, user_monthly_charge]])
predict = svc_modle.predict(user_input)
if predict[0] == 0:
    print("The customer likely to stay")
else:
    print("The customer unlikely to stay")