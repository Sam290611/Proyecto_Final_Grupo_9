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


def sd(data, columna):
    df=pd.read_csv(data)
    try:
        print( df[columna].std())
    except KeyError:
        return 'Error al procesar la columna'
    except Exception as e:
        return 'Error al procesar la columna'
def percentiles (datas, columna):
    try:
        assert columna in datas.columns, "La columna no existe en el DataFrame"
        percentil_25=datas[columna].quantile(0.25)
        percentil_50=datas[columna].quantile(0.50)
        percentil_75=datas[columna].quantile(0.75)
        return {"Percentil 25": percentil_25, "Percentil 50": percentil_50, "Percentil 75": percentil_75}
    except AssertionError as e:
        return str(e)
percentiles(datas,"NF")