import pandas as pd

datos = pd.read_csv("Trabajadores.csv", index_col="legajo")

#print(datos)
#datos = datos.dropna()

datos = datos.fillna(2000)

#print(datos[["nombre","hs_trabajadas"]])
#print(datos.loc[[108],["nombre","hs_trabajadas"]])
print(datos[(datos["hs_trabajadas"] >= 40) & (datos["valor_hora"] >= 2100)])

print(datos.describe())
