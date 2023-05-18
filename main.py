from data.data1 import apartamento1, apartamento2
import pandas as pd


tabla1 = pd.DataFrame(apartamento1, columns=['edad'])
tabla2 = pd.DataFrame(apartamento2,columns=['edad'])
tabla3 =pd.read_csv("./data/empleados.csv")



datosEstadisticosApto1 = tabla1.describe()
datosEstadisticosApto2 = tabla2.describe()
datosEstadisticosEmpresa = tabla3.describe()


print(datosEstadisticosApto1)
print("\n")
print(datosEstadisticosApto2)
print("\n")
print(datosEstadisticosEmpresa)