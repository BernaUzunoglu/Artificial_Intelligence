# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:59:13 2024

@author: BERNA
"""

import pandas as pd


# data = pd.read_csv("DataSets/melb_house_data.csv")
data = pd.read_csv("C:\\Users\\BERNA\\OneDrive\\Masaüstü\\Artificial_Intelligence\\ML_Algorithms_Models\\Decision_Trees\\DataSets\\melb_house_data.csv")
print(data.describe())# sayısal sutunlar şçin temel istatistikler.
print(data.columns)
#veri setinde nan alanlar vardı şimdilik o alanları kaldıralım.
data = data.dropna(axis=0)
# Tahmin etmesini istediğimiz alan
y = data.Price
# Tahmin etmek için kullanacağımız alanları belirleyelim. Bazı durumlarda tahmin için tüm alanlar kullanılırken bazen
# daha az alan dah iyi tahmin üretir. Gereken alanları kullanmak asıl mesele.

data_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = data[data_features]
print(X.describe())
print(X.head())

#Model oluşturulması
from sklearn.tree import DecisionTreeRegressor
# Modeli tanımlayın. Her çalıştırmada aynı sonuçların elde edilmesini sağlamak için random_state için bir sayı belirtin
data_model = DecisionTreeRegressor(random_state=1)
#Modelin eğitilmesi - bir kalıba oturtulması
data_model.fit(X,y)

print("Aşağıdaki 5 ev için tahminde bulunmak")
print(X.head())
print("Tahminler")
print(data_model.predict(X.head()))

from sklearn.metrics import mean_absolute_error
predicted_home_prices = data_model.predict(X)
print(mean_absolute_error(y,predicted_home_prices))

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
data_model = DecisionTreeRegressor()
#Fit model
data_model.fit(train_X,train_y)
val_prediction = data_model.predict(val_X)
print(mean_absolute_error(val_y,val_prediction))

#DecisionTreeRegression 
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):#mean absolute error değeri hesaplama
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))#Modelin en iyi 500 yaprakda MAE = 261.718 


#RandomForest Model
#Random Forest modelinin tahmini içinde bazı parametreler vardır. Fakat parametreler verilmese bile makul bir çalışma gerçeklleştirir.
from sklearn.ensemble import RandomForestRegressor
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))#Modelin MAE = 207.190 DecisionTreeRegression modeline göre daha iyi bir tahmin hata değeri