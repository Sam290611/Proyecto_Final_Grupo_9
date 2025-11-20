import pandas as pd
def promedios(nombre_archivo, nombre_columna):
    df= pd.read_csv(nombre_archivo)
    if nombre_columna not in df:
        raise  ValueError('Error al procesar la columna')
    else:
        def prom(x):
            p = 0
            for i in x:
                p += i
            promedio = p/len(x)
            return promedio
        return prom(df[nombre_columna])
    
promedios("/workspaces/Proyecto_Final_Grupo_9/TITANIC/test_Titanic.csv", "Age")