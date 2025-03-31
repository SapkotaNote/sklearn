
## We need to use different method
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
modle = LinearRegression()

# Features (Temperature, Humidity, Pressure)
X = np.array([
    [22.5, 60, 1012],
    [24.0, 55, 1013],
    [23.0, 58, 1014],
    [21.0, 62, 1010],
    [20.5, 64, 1011],
    [26.0, 50, 1015],
    [25.0, 53, 1016],
    [24.5, 55, 1017],
    [27.0, 47, 1018],
    [23.5, 60, 1012]
])

# Target (Class)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 0])


df = pd.DataFrame(X,y)
#print(df)

x_train, x_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=42)

modle.fit(x_train, y_train)

Temperature = float(input("Enter temperature: "))
Humidity = float(input("Enter Humidity: "))
Pressure = float(input("Enter Pressure: "))