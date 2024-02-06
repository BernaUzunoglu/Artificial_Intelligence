import matplotlib.pylab as plt
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn import datasets

diabetes = datasets.load_diabetes() # Scikit-learn kütüphanesinde yeralan diabet veri setini yüklüyoruz.

# Veri setimizi bir kısmını modeli eğitmek bir kısmınıda tes için kullnmak için gerekli modülü ve fonk yüklüyoruz.
from sklearn.model_selection import train_test_split
#diabetes.data => veri setindeki kullanılacak değişkenler
#diabetes.target => her hasta için hedef değişkenler
# X_train: Eğitim veri setinin özellik matrisi (features matrix).
# X_test: Test veri setinin özellik matrisi (features matrix).
# y_train: Eğitim veri setinin hedef değişkeni (target variable veya labels).
# y_test: Test veri setinin hedef değişkeni (target variable veya labels).
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=0)

#Model
model = LinearRegression()
model.fit(X_train,y_train)

#Matplotlib ile modelimizi çizelim
y_pred = model.predict(X_test)
plt.plot(y_test,y_pred,'.')

x = np.linspace(0,330,100)
y = x
plt.plot(x,y)
plt.show()