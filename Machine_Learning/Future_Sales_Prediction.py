import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("DataSets/advertising.csv")
print(data.head())

# Verimizin null değer içerip içermediğine bakalım
print(data.isnull().sum())

# Tv için sales amaount  verileri ile  arasındaki ilişkiyi görsellellştirelim.
import plotly.express as px 
import plotly.graph_objects as go
#Scatter- Dağılım grafiği ile görselleştirelim. Dağılım grafiiği iki değişken arasındaki ilişkiyi tespit etmede kullanılır.
figure = px.scatter(data_frame=data,
                    x="Sales",
                    y="TV",
                    trendline="ols")#ordinary least squares -  en küçük kareler, grafiğe çizgi çeker
figure.show()

# Gazete için sales amaount  verileri ile  arasındaki ilişkiyi görsellellştirelim.
figure = px.scatter(data_frame=data,
                    x="Sales",
                    y="Newspaper",
                    size="Newspaper",
                    trendline="ols")
figure.show()

# Radio için sales amaount  verileri ile  arasındaki ilişkiyi görsellellştirelim.
figure = px.scatter(data_frame=data,
                    x="Sales",
                    y="Radio",
                    size="Radio",
                    trendline="ols")
figure.show()

#Şimdi tüm sutunların satış sütunu ile arasındaki ilişkiye bakalım
correlation = data.corr()# iki değişken arasındaki ilişkinin gücünü ve yönünü ölçen bir istatistiksel kavramdır
print(correlation["Sales"].sort_values(ascending=False))

X = np.array(data.drop("Sales",axis=1))
y = np.array(data["Sales"])
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

#Model
model = LinearRegression()
model.fit(Xtrain,ytrain)
print(model.score(Xtest,ytest))

# girdilere göre hangi platformda ne kadar satış olacağını tahmin edelim
# alanlar = TV,Radio,Gazete
features = np.array([[230.1,37.8,69.2]])
print("Tahmin")
print(model.predict(features))