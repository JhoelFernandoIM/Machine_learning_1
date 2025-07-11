#importando las librerias
import pandas as pd
import joblib
import os

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, r2_score


#cargar datos
ruta_base = os.path.dirname(os.path.dirname(__file__))
ruta_csv = os.path.join(ruta_base, 'data_sintetica', 'farmacologia_recuperacion.csv')

df = pd.read_csv(ruta_csv)

#variables
X = df[['edad', 'peso', 'dosis']]
y = df['tiempo_recuperacion']

#Division de datos para train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Entrenar el modelo lineal
modelo_lineal = LinearRegression()
modelo_lineal.fit(X_train, y_train)

#Guardar el modelo
os.makedirs('entrenamiento/regresion_lineal.pkl')

#Evaluar
y_pred = modelo_lineal.predict(X_test)
print(f"R2: {r2_score(y_test, y_pred):.2f}")
print(f"RMSE: {root_mean_squared_error(y_test, y_pred):.2f}")