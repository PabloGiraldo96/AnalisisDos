import pandas as pd
from data.data1 import apartamento1, apartamento2
from helpers.tablasHTML import crearTabla
from helpers.graficas import graficar_salario
from helpers.graficandoTorta import graficarTorta 



tabla1 = pd.DataFrame(apartamento1, columns=['edad'])
tabla2 = pd.DataFrame(apartamento2, columns=['edad'])

tabla3 =pd.read_csv("./data/empleados.csv")

# Filtrando y aplicando condiciones 

analistas1 = tabla3.query('cargo == "analista1"')

analistas2 = tabla3.query('cargo == "analista2"')

empleadosMayores = tabla3.query('edad >= 50')

empleadosJovenes = tabla3.query('edad <= 30')

promedio_analistas1 = tabla3.query('cargo == "analista1"')['salario'].mean()

limpiado = empleadosJovenes.isna("-")
limpiado = empleadosJovenes.isin("-")



datos_uno = tabla3.describe()

print(promedio_analistas1)
print(f"El promedio de salarios es: {promedio_analistas1}")


# Generacion de tablas 

# crearTabla(analistas1, "analistas 1")
# crearTabla(analistas2, "analistas 2")
# crearTabla(empleadosMayores, "Jubilados")
# crearTabla(empleadosJovenes, "Jovenes")

# Generacion de graficas

# graficar_salario(empleadosMayores, 'cargo', 'salario', 'PromedioSalarios') 

# graficarTorta(analistas1, [20, 30, 40, 50, 60], 'edad', 'salario', 'promediosAnalistasUno')

