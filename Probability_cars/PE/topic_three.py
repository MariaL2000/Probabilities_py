import pandas as pd
import numpy as np
import scipy.stats as stats

def muestreo_y_estimacion(df):
    """Calcula la frecuencia absoluta, relativa y acumulada de marcas con aceleración mayor a 15."""
    
    # Filtrar vehículos con aceleración mayor a 15
    vehiculos_aceleracion_mayor_15 = df[df['acceleration'] > 15]
    
    # Contar cuántos vehículos hay por marca
    frecuencia_absoluta = vehiculos_aceleracion_mayor_15['name'].value_counts()
    
    # Crear un DataFrame para almacenar los resultados
    resultados = pd.DataFrame(frecuencia_absoluta).reset_index()
    resultados.columns = ['Marca', 'Frecuencia Absoluta']
    
    # Calcular la frecuencia relativa
    total_vehiculos = len(df)
    resultados['Frecuencia Relativa'] = resultados['Frecuencia Absoluta'] / total_vehiculos
    
    # Calcular la frecuencia acumulada
    resultados['Frecuencia Acumulada'] = resultados['Frecuencia Absoluta'].cumsum()
    
    # Ordenar el DataFrame por marca
    resultados = resultados.sort_values(by='Marca').reset_index(drop=True)
    
    return resultados




def marca_con_mayor_horsepower(df):
    """Devuelve la marca con mayor horsepower."""
    max_horsepower_row = df.loc[df['horsepower'].idxmax()]
    return max_horsepower_row['name'], max_horsepower_row['horsepower']

def estimacion_puntual_media_horsepower(df):
    """Calcula la estimación puntual de la media del horsepower."""
    media_horsepower = df['horsepower'].mean()
    return media_horsepower

def intervalo_confianza_horsepower(df, marca, confianza=0.95):
    """Obtiene el intervalo de confianza del 95% para el horsepower de una marca específica."""
    marca_df = df[df['name'].str.contains(marca, case=False)]
    
    if len(marca_df) == 0:
        return None  # Si no hay vehículos de la marca especificada
    
    n = len(marca_df)
    media = marca_df['horsepower'].mean()
    std_dev = marca_df['horsepower'].std()
    
    # Calcular el error estándar
    error_estandar = std_dev / np.sqrt(n)
    
    # Calcular el intervalo de confianza
    z = stats.norm.ppf((1 + confianza) / 2)  # Valor crítico para el nivel de confianza
    intervalo = (media - z * error_estandar, media + z * error_estandar)
    
    return intervalo

def porcentaje_marca_mayor_horsepower(df):
    """Calcula el porcentaje que representa la marca de autos con mayor horsepower del total."""
    marca, _ = marca_con_mayor_horsepower(df)
    total_vehiculos = len(df)
    vehiculos_marca = len(df[df['name'].str.contains(marca, case=False)])
    
    if total_vehiculos > 0:
        porcentaje = (vehiculos_marca / total_vehiculos) * 100
    else:
        porcentaje = 0
    
    return porcentaje