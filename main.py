from data.data1 import apartamento1, apartamento2
from helpers.tablasHTML import crearTabla
import pandas as pd


tabla1 = pd.DataFrame(apartamento1, columns=['edad'])
tabla2 = pd.DataFrame(apartamento2,columns=['edad'])
tabla3 =pd.read_csv("./data/empleados.csv")


# Filtrando y aplicando condiciones 

empleadosJovenes = tabla3.query('edad < 28 and cargo == "analista1"')

analistas1 = tabla3.query('cargo == "analista1"')

analistas2 = tabla3.query('cargo == "analista2"')

empleadosMayores = tabla3.query('edad >= 50')


# Generacion de tablas 

crearTabla(analistas1, "analistas 1")
crearTabla(analistas2, "analistas 2")
crearTabla(empleadosMayores, "Jubilados")
