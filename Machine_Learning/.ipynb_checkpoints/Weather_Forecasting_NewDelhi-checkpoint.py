import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

data = pd.read_csv("DataSets/DailyDelhiClimateTrain.csv")
print(data.head())

# Veri setinin genel istatistik verilerine bakalım
print(data.describe())
# Kolonlarda ki veriler içeriğine bir bakalım
print(data.info())
# Datetime tipi yoktur tarih object olarak verilmiş. Gerekirse veri tipi dönüşümü yapılacaktır.

#Yeni Delhi yıllara göre ortalama sıcaklık grafiği
figure = px.line(data,x="date",
                 y="meantemp",
                 title="Mean Temperature in Delhi Over the Years'")
figure.show()

#Yeni Delhi yıllara göre  nem(humidity) grafiği
figure = px.line(data,x="date",
                 y="humidity",
                 title="Humidity in Delhi Over the Years'")
figure.show()

#Yeni Delhi yıllara göre  rüzgar hızı(wind_speed) grafiği
figure = px.line(data,x="date",
                 y="wind_speed",
                 title="Wind Speed Delhi Over the Years'")
figure.show()

#Sıcaklık ve nem arasındaki ilişki
figure = px.scatter(data_frame=data,
                    x="humidity",
                    y="meantemp",
                    size="meantemp",
                    trendline="ols",
                    title="Relationship Between Temperature and Humidity")
figure.show() # Sıcaklık ve nem arasında ters orantı var sıcaklık fazla ise nem az ,sıcaklık az ise nem çok - negatif bir ilişki var

#Date olan alanın veri tipi object , datetime yapalım
data["date"] = pd.to_datetime(data["date"],format='%Y-%m-%d')
data["year"] = data["date"].dt.year
data["month"] = data["date"].dt.month
print(data.head())

# Delhi'deki sıcaklık değişimini yıllara göre gösteren bir çizgi grafiği oluşturalım
plt.style.use('fivethirtyeight')
plt.figure(figsize=(15, 10))
plt.title("Temperature Change in Delhi Over the Years")
sns.lineplot(data = data, x='month', y='meantemp', hue='year')
plt.show()# yıllara göre graiğe baktığımızda yaz aylarında sıcaklığın en çok olduğu ve yıllara göre bir artış olduğu gözlemlenir.

#Facebook Prophet(Peygamber) Model ile hava tahmini 
'''Bu model zaman serisi tahminleri için en iyi tekniklerden biridir.'''
forecast_data = data.rename(columns={"date" : "ds", "meantemp" :"y"})
print(forecast_data)

from prophet import Prophet
from prophet.plot import plot_plotly#,plot_components_plotly
import plotly.offline as pyo
pyo.init_notebook_mode(connected=True)

model = Prophet()
model.fit(forecast_data)
forecasts = model.make_future_dataframe(periods=365)
predictions = model.predict(forecasts)
plot_plotly(model,predictions)


