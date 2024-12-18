
import pandas as pd
import scipy.stats as stats

def prueba_hipotesis_una_poblacion(df):
    """Realiza una prueba de hipótesis para una población (Ford Galaxie 500)."""
    
    # Filtrar los Ford Galaxie 500
    ford_galaxie = df[df['name'].str.contains('ford galaxie 500', case=False)]
    
    # Hipótesis nula: La media del peso de los Ford Galaxie 500 es mayor que un valor específico (por ejemplo, 4000 lbs)
    media_hipotetica = 4000
    alpha = 0.05  # Nivel de significancia
    
    if len(ford_galaxie) == 0:
        return None  # No hay datos para Ford Galaxie 500
    
    # Calcular la media y la desviación estándar
    media_muestra = ford_galaxie['weight'].mean()
    std_muestra = ford_galaxie['weight'].std()
    n = len(ford_galaxie)
    
    # Calcular el estadístico de prueba (t)
    t_stat = (media_muestra - media_hipotetica) / (std_muestra / (n ** 0.5))
    
    # Calcular el valor p
    p_value = stats.t.sf(t_stat, df=n-1)  # Prueba de una cola
    
    # Decisión
    if p_value < alpha:
        resultado = "Rechazamos la hipótesis nula: Los Ford Galaxie 500 son más pesados que 4000 lbs."
    else:
        resultado = "No rechazamos la hipótesis nula: No hay evidencia suficiente para afirmar que los Ford Galaxie 500 son más pesados que 4000 lbs."
    
    return resultado, media_muestra, p_value

def prueba_hipotesis_dos_poblaciones(df, marca1, marca2):
    """Realiza una prueba de hipótesis para dos poblaciones."""
    
    # Filtrar las dos marcas
    muestra1 = df[df['name'].str.contains(marca1, case=False)]['weight']
    muestra2 = df[df['name'].str.contains(marca2, case=False)]['weight']
    
    # Hipótesis nula: No hay diferencia en los pesos medios de las dos marcas
    alpha = 0.05  # Nivel de significancia
    
    # Realizar la prueba t para dos muestras independientes
    t_stat, p_value = stats.ttest_ind(muestra1, muestra2, equal_var=False)  # Asumimos varianzas desiguales
    
    # Decisión
    if p_value < alpha:
        resultado = f"Rechazamos la hipótesis nula: Hay una diferencia significativa en los pesos entre {marca1} y {marca2}."
    else:
        resultado = f"No rechazamos la hipótesis nula: No hay evidencia suficiente para afirmar que hay una diferencia en los pesos entre {marca1} y {marca2}."
    
    return resultado, t_stat, p_value

def prueba_hipotesis_mas_dos_poblaciones(df, marcas):
    """Realiza una prueba de hipótesis para más de dos poblaciones (ANOVA)."""
    
    # Filtrar las muestras para las marcas especificadas
    muestras = [df[df['name'].str.contains(marca, case=False)]['weight'] for marca in marcas]
    
    # Hipótesis nula: No hay diferencia en los pesos medios de las marcas
    alpha = 0.05  # Nivel de significancia
    
    # Realizar la prueba ANOVA
    f_stat, p_value = stats.f_oneway(*muestras)
    
    # Decisión
    if p_value < alpha:
        resultado = "Rechazamos la hipótesis nula: Hay una diferencia significativa en los pesos entre las marcas."
    else:
        resultado = "No rechazamos la hipótesis nula: No hay evidencia suficiente para afirmar que hay una diferencia en los pesos entre las marcas."

    return resultado, f_stat, p_value