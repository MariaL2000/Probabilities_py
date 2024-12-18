# topic_two.py

import pandas as pd
from scipy.stats import binom

def probabilidad_toyota_corona_mpg(df):
    """Calcula la probabilidad de que los Toyota Corona tengan un mpg >= 20 usando la distribución binomial."""
    
    # Filtrar los Toyota Corona
    toyota_corona = df[df['name'].str.contains('toyota corona', case=False)]
    
    # Total de Toyota Corona
    n = len(toyota_corona)
    
    # Contar cuántos Toyota Corona tienen mpg >= 20
    exitos = len(toyota_corona[toyota_corona['mpg'] >= 20])
    
    # Probabilidad de éxito (p)
    if n > 0:
        p = exitos / n
    else:
        p = 0
    
    # Usar la distribución binomial para calcular la probabilidad de que al menos un Toyota Corona tenga mpg >= 20
    probabilidad_al_menos_uno = 1 - binom.pmf(0, n, p)
    
    return probabilidad_al_menos_uno

def probabilidad_toyota_corona_mpg_entre_20_y_25(df):
    """Calcula la probabilidad de que los Toyota Corona tengan un mpg entre 20 y 25 usando la distribución binomial."""
    
    # Filtrar los Toyota Corona
    toyota_corona = df[df['name'].str.contains('toyota corona', case=False)]
    
    # Total de Toyota Corona
    n = len(toyota_corona)
    
    # Contar cuántos Toyota Corona tienen mpg entre 20 y 25
    exitos = len(toyota_corona[(toyota_corona['mpg'] >= 20) & (toyota_corona['mpg'] <= 25)])
    
    # Probabilidad de éxito (p)
    if n > 0:
        p = exitos / n
    else:
        p = 0
    
    # Usar la distribución binomial para calcular la probabilidad de que al menos un Toyota Corona tenga mpg entre 20 y 25
    probabilidad_al_menos_uno = 1 - binom.pmf(0, n, p)
    
    return probabilidad_al_menos_uno

def valor_esperado_aceleracion(df):
    """Calcula el valor esperado (media) de la aceleración de los Toyota Corona."""
    
    # Filtrar los Toyota Corona
    toyota_corona = df[df['name'].str.contains('toyota corona', case=False)]
    
    # Calcular la media de la aceleración
    if len(toyota_corona) > 0:
        media_aceleracion = toyota_corona['acceleration'].mean()
    else:
        media_aceleracion = 0
    
    return media_aceleracion