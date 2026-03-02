import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , mean_squared_error ,r2_score
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pickle

dataset = pd.read_csv(r"E:\Work\Programs\Python\AI\Machine Learning\Projects\House Price Predictator\data\cityhome_data.csv")
dataset.dropna(inplace=True)

print(dataset)

le = LabelEncoder()
dataset["House_condition(Encoded)"] = le.fit_transform(dataset["House_Condition"])
dataset["Location(Encoded)"] = le.fit_transform(dataset["Location"])
columns = dataset[["Size_SqFt" , "Bedrooms", "Bathrooms" , "Location(Encoded)" ,
                    "House_condition(Encoded)" , "Year_Built"]]

X = columns
y = dataset["Price"]
X_train  , X_test , y_train , y_test = train_test_split(X , y , test_size=0.2 , random_state=42)

print(dataset)

model = LinearRegression()

model.fit(X_train , y_train)
predicted_Test = model.predict(X_test)

mse= mean_squared_error(y_test , predicted_Test)
mae = mean_absolute_error(y_test , predicted_Test)
r2 =  r2_score(y_test , predicted_Test)
print("Mse: " , round(mse))
print("Rmse: " , round(np.sqrt(mse)))
print("Mae: " , round(mae))
print("R2 score: " , r2*100 , "%")


data_to_save = {
    "model": model
}

try:
    with open(r'E:\Work\Programs\Python\AI\Machine Learning\Projects\House Price Predictator\model\cityhome.pkl', 'wb') as file:
        pickle.dump(data_to_save, file)
    print("Model saved successfully!")
except Exception as e:
    print("Error while saving:", e)

