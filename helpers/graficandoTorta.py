import matplotlib.pyplot as plt
import pandas as pd 



def graficarTorta(dataFrame, rangos, columnaInteresRango, columnaAPromediar, nombre):

    figura = plt.figure()
    
    #Crear nueva columna con los rangos
    
    dataFrame['rangoNuevo']= pd.cut(dataFrame[columnaInteresRango], bins = rangos)

    # Calcular la suma de los salarios por cada rango
    
    salarioPorRango = dataFrame.groupby('rangoNuevo')[columnaAPromediar].sum()
    
    # Obtener los datos de salario y rango edad 
    
    salario =salarioPorRango.values
    rangosEdad = salarioPorRango.index
    
    # Se crea la torta 

    plt.pie(salario, labels = rangosEdad, autopct='%1.1f%%')
    
    plt.title("Distribucion de salarios por rango de edad")
    
    plt.savefig(f'./assets/img/{nombre}.png' , dpi = 300, bbox_inches ='tight')