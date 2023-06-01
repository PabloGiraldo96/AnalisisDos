import pandas as pd
from data.data1 import apartamento1, apartamento2
from helpers.tablasHTML import crearTabla


tabla1 = pd.DataFrame(apartamento1, columns=['edad'])
tabla2 = pd.DataFrame(apartamento2, columns=['edad'])

tabla3 =pd.read_csv("./data/empleados.csv")


# Filtrando y aplicando condiciones 

analistas1 = tabla3.query('cargo == "analista1"')

analistas2 = tabla3.query('cargo == "analista2"')

empleadosMayores = tabla3.query('edad >= 50')

empleadosJovenes = tabla3.query('edad <= 30')

#promedio_analistas1 = tabla3.query('cargo == "analistas1"')['salario'].mean()

datos_uno = tabla3.describe()

datos = datos_uno['salario'].mean()

print(datos_uno)
print(f"El promedio de salarios es: {datos}")


# Generacion de tablas 

crearTabla(analistas1, "analistas 1")
crearTabla(analistas2, "analistas 2")
crearTabla(empleadosMayores, "Jubilados")
crearTabla(empleadosJovenes, "Jovenes")
