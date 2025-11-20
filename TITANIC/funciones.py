import pandas as pd
def promedios(nombre_archivo, nombre_columna):
    df= pd.read_csv(nombre_archivo)
    if nombre_columna not in df.columns:
        raise  ValueError('Error al procesar la columna')
    def prom(x):
        p = 0
        for i in x:
            p += i
        promedio = p/len(x)
        return promedio
    return prom(df[nombre_columna])
