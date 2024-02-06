import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go 

data = pd.read_csv("DataSets/Waiter_Tips.csv")
print(data.head())
#veri setindeki size etiketi kişi sayısı

#günlere göre bahşiş oranı inceleyelim 
figure = px.scatter(data_frame=data,
                    x="total_bill",
                    y="tip",
                    size="size",
                    color="day",
                    trendline="ols")
figure.show()

#cinsiyete göre bahşiş oranını inceleyelim
figure = px.scatter(data_frame=data,
                    x="total_bill",
                    y="tip",
                    size="size",
                    color="sex",
                    trendline="ols")
figure.show() # erkeklerin bahşiş olasılığı daha iyi

#yemek vaktine göre bahşiş oranını inceleyelim
figure = px.scatter(data_frame=data,
                    x="total_bill",
                    y="tip",
                    size="size",
                    color="time",
                    trendline="ols")
figure.show() # akşam yemeği öğle yemeğine göre bahşiş olasılığı daha yüksek

#Şimdi garsonlara hangi gün en çok bahşiş verilmiş bakalım
figure = px.pie(data,
                values="tip",
                names='day',
                hole=0.5) # daire içine boşluk oluşturma
figure.show()#sonuçlara göre en çok bahşiş cumartesi veriliyor.

figure = px.pie(data,
                values="tip",
                names='sex',
                hole=0.5)
figure.show()#sonuçlara göre en çok bahşiş erkekler veriyor.

figure = px.pie(data,
                values="tip",
                names='smoker',
                hole=0.5)
figure.show()#sonuçlara göre en çok bahşiş sigara içmeyenler veriyor.

figure = px.pie(data,
                values="tip",
                names='time',
                hole=0.5)
figure.show()#sonuçlara göre en çok bahşiş akşam yemeklerinde daha çok bahşiş veriliyor.

#veri setindeki kategorik verileri sayısal verilere çevirelim

data["sex"] = data["sex"].map({"Female": 0, "Male": 1})
data["smoker"] = data["smoker"].map({"No": 0, "Yes": 1})
data["day"] = data["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
data["time"] = data["time"].map({"Lunch": 0, "Dinner": 1})
print(data.head())

x = np.array(data[["total_bill", "sex", "smoker", "day", 
                   "time", "size"]])
y = np.array(data["tip"])

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.2, 
                                                random_state=42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xtrain, ytrain)

# features = [[total_bill, "sex", "smoker", "day", "time", "size"]]
# toplam hesap 24,50 ödenen,sigara içmeyen perşembe günü akşam yemeğinde 4 kişilik bir erkek grubu bahşiş verme olasılığı tahmin etme
features = np.array([[24.50, 1, 0, 0, 1, 4]])
print(model.predict(features))

features = np.array([[50.50, 1, 0, 2, 1, 6]])
print(model.predict(features))