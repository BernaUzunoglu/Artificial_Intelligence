import pandas as pd 
import numpy as np 
import plotly.express as px #Çok çeşitli istatistiksel, finansal, coğrafi, bilimsel ve 3 boyutlu kullanım durumlarını kapsayan 40'tan fazla benzersiz grafik türünü destekleyen çizim kitaplığı.
import plotly.graph_objects as go 
import plotly.io as pio #grafiklerin, çizimlerin ve diğer görsel öğelerin görünümünü ayarlamak için kullanılır.
pio.templates.default = "plotly_white" 

data = pd.read_csv("DataSets/Credit_Score_Data.csv")
# data = pd.read_csv("C:\\Users\\BERNA\\OneDrive\\Masaüstü\\Artificial_Intelligence\\Machine_Learning\\DataSets\\Credit_Score_Data.csv")
print(data.head(10))
print(data.info())

#null değer kontrolü
print(data.isnull().sum())#hiçbir sutunda null değer yoktur.

#Kredi skor değerlerine bir bakalım
print(data["Credit_Score"].value_counts())

# Kredi puanını etkileyen değişkenler
#Meslekler kredi puanını etkiliyor mu bakalım?
fig = px.box(data,
             x = "Occupation",
             color = "Credit_Score",
             title = "Credit Scores Based on Occupation",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.show() # kayda değer bir farklılık yoktur.

#Yıllık gelir(Annual Income) kredi puanını etkiliyor mu bakalım?
fig = px.box(data,
             x="Credit_Score", 
            y="Annual_Income",
             color="Credit_Score",
             title="Credit Scores Based on Annual_Income",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive") # Kutu grf. quartilemethod çeyrek değerleri hesaplama yön.exclusive kutunun dışındaki verileride içerir.
fig.show()#yıllık elde edilen gelire göre kredi puanı artmaktadır.

#Aylık Maaşa(Monthly Salary) göre kredi puanını etkiliyor mu bakalım?
fig = px.box(data,
             x="Credit_Score", 
            y="Monthly_Inhand_Salary",
             color="Credit_Score",
             title="Credit Scores Based on Monthly_Inhand_Salary",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()#aylık elde edilen gelire göre kredi puanı artmaktadır.


#Daha fazla banka hesabına sahip olmak kredi puanını etkiliyor mu bakalım?
fig = px.box(data,
             x="Credit_Score", 
            y="Num_Bank_Accounts",
             color="Credit_Score",
             title="Credit Scores Based on Num_Bank_Accounts",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()# Daha fazla banka hesabı olması kredi puanı için iyi değildir.


#Daha fazla kredi kartına sahip olmak kredi puanını etkiliyor mu bakalım?
fig = px.box(data,
             x="Credit_Score", 
            y="Num_Credit_Card",
             color="Credit_Score",
             title="Credit Scores Based on Num_Credit_Card",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()# Daha fazla kredi kartına sahip olmak kredi puanı için iyi değildir.

#Kredilere falan ödenilen faiz(Interest_Rate) tutarı kredi puanını etkiliyor mu bakalım?
fig = px.box(data,
             x="Credit_Score", 
            y="Interest_Rate",
             color="Credit_Score",
             title="Credit Scores Based on Interest_Rate",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()# Faiz oranı 4-11 arası ise iyi, giderek artarsa kötü yönde etkiliyor.

#Şimdi iyi bir kredi puanı için tek seferde kaç kredi(Num_of_Loan) alabileceğimize bakalım.
fig = px.box(data,
             x="Credit_Score", 
            y="Num_of_Loan",
             color="Credit_Score",
             title="Credit Scores Based on Num_of_Loan",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()#Kredi başvuru sayısı artıkça kredi puanı ters orantılı gidiyor.

#Şimdi  ödemeleri vadesinde geciktirmenin kredi puanını nasıl etkilediğine  bakalım.
fig = px.box(data,
             x="Credit_Score", 
            y="Delay_from_due_date",
             color="Credit_Score",
             title="Credit Scores Based  on Average Number of Days Delayed f",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()#Kredi ödemelerimizi 5 ila 14 güne kadar geciktirip erteleyebiliriz. fazlası olunca kredi puanı git gide düşüyor.

#Şimdi  ödemeleri sık sık ertelemenin kredi puanını nasıl etkilediğine  bakalım.
fig = px.box(data,
             x="Credit_Score", 
            y="Num_of_Delayed_Payment",
             color="Credit_Score",
             title="Credit Scores Based  on Average Num_of_Delayed_Payment",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()#Kredi ödemelerimizi 4 ila 10 güne kadar erteleyebiliriz. fazlası olunca kredi puanı git gide düşüyor.

#Şimdi  fazla ödenmemiş borç(Outstanding_Debt) kredi puanını nasıl etkilediğine  bakalım.
fig = px.box(data,
             x="Credit_Score", 
            y="Outstanding_Debt",
             color="Credit_Score",
             title="Credit Scores Based  on Outstanding_Debt",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()#Kredi borcu arttıkça kredi puanıda düşüyor.Belirli miktar borcu geçince kredi puanı düşüyor.

#Şimdi kredi kullanım oranının yüksek olmasının  kredi puanını nasıl etkilediğine  bakalım.
fig = px.box(data,
             x="Credit_Score", 
            y="Credit_Utilization_Ratio",
             color="Credit_Score",
             title="Credit Scores Based  on Credit_Utilization_Ratio",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()#Grafikte kredi kullanım oranı kredi puanı için büyük bir etken değildir.

#Şimdi aylık yatırımlarınızın  kredi puanını nasıl etkilediğine  bakalım.
fig = px.box(data,
             x="Credit_Score", 
            y="Amount_invested_monthly",
             color="Credit_Score",
             title="Credit Scores Based  on Amount_invested_monthly",
             color_discrete_map={'Poor' :'red',
                                 'Standard':'yellow',
                                 'Good' : 'green'})
fig.update_traces(quartilemethod = "exclusive")
fig.show()#Grafikte aylık yatırdığınız para miktarı kredi puanlarınızı çok fazla etkilemez az etkiler.

#Credit_Mix = > Alınan kredi türlerini belirtir.Kredit Mix alanı kategorize edilmiş bir alan gösterebilmek için sayısal ifadelere dönüştürmek gerek.
#Standard =1
#Good = 2
#Bad = 0

data["Credit_Mix"] = data["Credit_Mix"].map({"Standard": 1, 
                               "Good": 2, 
                               "Bad": 0})
print(data["Credit_Mix"])

from sklearn.model_selection import train_test_split # veri setini eğitim ve test setlerine bölme işlevini gerçekleştirmek için kullanılır.
x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary", 
                   "Num_Bank_Accounts", "Num_Credit_Card", 
                   "Interest_Rate", "Num_of_Loan", 
                   "Delay_from_due_date", "Num_of_Delayed_Payment", 
                   "Credit_Mix", "Outstanding_Debt", 
                   "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data[["Credit_Score"]])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                    test_size=0.33, 
                                                    random_state=42) #test_size param. değ. ile veri setinin 0,33 nü test verisi olarak kullanıyoruz.
from sklearn.ensemble import RandomForestClassifier 
'''Rastge leAğaç Sınıflandırması, özellik alt kümesini kullanarak eğitilir ve bu ağaçların sonuçları bir araya getirilerek daha güçlü ve genelleştirilebilir bir model 
elde edilir'''
# RandomForestClassifier modelini oluştur
model = RandomForestClassifier() 
# Modeli eğit
model.fit(xtrain, ytrain)

print("Credit Score Prediction : ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))


features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
print("Predicted Credit Score = ", model.predict(features))# geliştirilen modelde yeni girdilere göre tahmin yapar.

''' Girdiler ve Çıktı
Credit Score Prediction : 
Annual Income: 19114.12
Monthly Inhand Salary: 1824.843333
Number of Bank Accounts: 2
Number of Credit cards: 2
Interest rate: 9
Number of Loans: 2
Average number of days delayed by the person: 12
Number of delayed payments: 3
Credit Mix (Bad: 0, Standard: 1, Good: 3) : 3
Outstanding Debt: 250
Credit History Age: 200
Monthly Balance: 310
Predicted Credit Score =  ['Good']
PS C:\Users\BERNA\OneDrive\Masaüstü\Artificial_Intelligence\Machine_Learning> 
'''