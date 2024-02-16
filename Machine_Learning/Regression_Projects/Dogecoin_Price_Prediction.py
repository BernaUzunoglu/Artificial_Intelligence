import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.ensemble import RandomForestRegressor 

data = pd.read_csv("DataSets/DOGE-USD.csv") 
print(data.head())
print(data['Date'].dtype)
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
print(data['Date'].dtype)
data.set_index('Date', inplace=True) 
data.corr() #sütunlar arasındaki korelasyonu (ilişkiyi) hesaplar 1,-1 yakın olursa güçlü 0 yakın olursa zayıf. pozitif,negatif yönlü oluyor
# null değerlerin olulp olmadığını kontrol edelim.
print(data.isnull().any()) 
print(data.isnull().sum())
#hata yapmamamk için eksik verileri çıkaralım
data = data.dropna()
print(data.describe()) # verilerin istatistiksel değerlerini kontrol edelim mean-max vs.

# Kapanış fiyatını analiz edelim.
plt.figure(figsize=(20, 7)) 
x = data.groupby('Date')['Close'].mean() 
x.plot(linewidth=2.5, color='b') 
plt.xlabel('Date') 
plt.ylabel('Volume') 
plt.title("Date vs Close of 2021") 
# plt.show()

# verileri 
data["gap"] = (data["High"] - data["Low"]) * data["Volume"] 
data["y"] = data["High"] / data["Volume"] 
data["z"] = data["Low"] / data["Volume"] 
data["a"] = data["High"] / data["Low"] 
data["b"] = (data["High"] / data["Low"]) * data["Volume"] 
#Close sütunu ile diğer sütunlar arasındaki korelasyonların mutlak değerleri hesaplayalım.
abs(data.corr()["Close"].sort_values(ascending=False)) # azalan sırada düzenliyoruz.


data = data[["Close", "Volume", "gap", "a", "b"]] 
print(data.head()) 

df2 = data.tail(30) 
train = df2[:11] 
test = df2[-19:] 

print(train.shape, test.shape) 

#Model
from statsmodels.tsa.statespace.sarimax import SARIMAX 
model = SARIMAX(endog=train["Close"], exog=train.drop( 
	"Close", axis=1), order=(2, 1, 1)) 
results = model.fit() 
print(results.summary()) 

#şimdi zaman serisindeki tahminleri gözlemleyelim
start = 11
end = 29
predictions = results.predict( 
	start=start, 
	end=end, 
	exog=test.drop("Close", axis=1)) 
print(predictions) 


test["Close"].plot(legend=True, figsize=(12, 6))
predictions.plot(label='TimeSeries', legend=True)

