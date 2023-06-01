import matplotlib.pyplot as plt



def graficar_salario(dataframe, columnX, columnY, name):
    
#Lista de colores 
    
    colores = ['green', 'red', 'blue']
    
#Obtener promedio de salarios

    salarioPromedio = dataframe.groupby(columnX)[columnY].mean()

# Graficar 

    plt.bar(salarioPromedio.index, salarioPromedio, color = colores)
    plt.xlabel("Cargo")
    plt.ylabel("Promedio de salario")
    plt.title("TABLA PROMEDIOS POR CARGO ")

# Guardo grafica

    plt.savefig(f'./assets/img/{name}.png' , dpi = 300, bbox_inches ='tight')