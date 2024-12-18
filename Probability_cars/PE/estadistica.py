import pandas as pd
import os
from topic_one import probabilidad_coche_usa, probabilidad_volvo_europa, probabilidad_horsepower_usa
from topic_two import probabilidad_toyota_corona_mpg, probabilidad_toyota_corona_mpg_entre_20_y_25, valor_esperado_aceleracion
from topic_three import (
    muestreo_y_estimacion,
    marca_con_mayor_horsepower,
    estimacion_puntual_media_horsepower,
    intervalo_confianza_horsepower,
    porcentaje_marca_mayor_horsepower
)

from topic_fourth import (
    prueba_hipotesis_una_poblacion,
    prueba_hipotesis_dos_poblaciones,
    prueba_hipotesis_mas_dos_poblaciones
)

# Definir la ruta del archivo CSV
file_path = r'C:\ALMACEN\UCI\Probability_cars\PE\mpg.csv'

# Leer el archivo CSV
try:
    df = pd.read_csv(file_path)
    print("Datos cargados correctamente.")
except FileNotFoundError:
    print(f"El archivo no se encontró en la ruta: {file_path}")
    exit()


# Calcular y mostrar las probabilidades usando los métodos importados
prob_usa = probabilidad_coche_usa(df)
print(f"\nProbabilidad de que un coche provenga de USA: {prob_usa:.2f}")

prob_volvo_europa = probabilidad_volvo_europa(df)
print(f"Probabilidad de que un coche provenga de Europa y sea un Volvo: {prob_volvo_europa:.2f}")

prob_horsepower_usa = probabilidad_horsepower_usa(df)
print(f"Probabilidad de que un coche provenga de USA y tenga un horsepower >= 220: {prob_horsepower_usa:.2f}")




# Calcular y mostrar la probabilidad de que los Toyota Corona tengan un mpg >= 20
prob_toyota_corona_mpg = probabilidad_toyota_corona_mpg(df)
print(f"Probabilidad de que los Toyota Corona tengan un mpg >= 20: {prob_toyota_corona_mpg:.2f}")

# Calcular y mostrar la probabilidad de que los Toyota Corona tengan un mpg entre 20 y 25
prob_toyota_corona_mpg_entre_20_y_25 = probabilidad_toyota_corona_mpg_entre_20_y_25(df)
print(f"Probabilidad de que los Toyota Corona tengan un mpg entre 20 y 25: {prob_toyota_corona_mpg_entre_20_y_25:.2f}")

# Calcular y mostrar el valor esperado de la aceleración de los Toyota Corona
media_aceleracion = valor_esperado_aceleracion(df)
print(f"Valor esperado de la aceleración de los Toyota Corona: {media_aceleracion:.2f} unidades")






# Calcular y mostrar la tabla de muestreo y estimación
resultados_muestreo = muestreo_y_estimacion(df)
print("\nTabla de marcas con aceleración mayor a 15:")
print(resultados_muestreo)


# Obtener la marca con mayor horsepower
marca, horsepower_max = marca_con_mayor_horsepower(df)
print(f"Marca con mayor horsepower: {marca} con {horsepower_max} hp")

# Calcular y mostrar la estimación puntual de la media del horsepower
media_horsepower = estimacion_puntual_media_horsepower(df)
print(f"Estimación puntual de la media del horsepower: {media_horsepower:.2f} hp")


# Calcular y mostrar el intervalo de confianza del 95% para una marca específica
marca_especifica = "Toyota"  # Cambia esto por la marca que desees
intervalo_confianza = intervalo_confianza_horsepower(df, marca_especifica)
if intervalo_confianza:
    print(f"Intervalo de confianza del 95% para {marca_especifica}: {intervalo_confianza}")

# Calcular y mostrar el porcentaje que representa la marca de autos con mayor horsepower
porcentaje = porcentaje_marca_mayor_horsepower(df)
print(f"Porcentaje de la marca con mayor horsepower del total: {porcentaje:.2f}%")







# Prueba de hipótesis para una población (Ford Galaxie 500)
resultado_una_poblacion, media_muestra, p_value_una = prueba_hipotesis_una_poblacion(df)
print(f"Resultado prueba una población: {resultado_una_poblacion}, Media muestra: {media_muestra:.2f}, p-value: {p_value_una:.4f}")

# Prueba de hipótesis para dos poblaciones
marca1 = "Toyota"
marca2 = "Ford"
resultado_dos_poblaciones, t_stat, p_value_dos = prueba_hipotesis_dos_poblaciones(df, marca1, marca2)
print(f"Resultado prueba dos poblaciones: {resultado_dos_poblaciones}, t-stat: {t_stat:.4f}, p-value: {p_value_dos:.4f}")

# Prueba de hipótesis para más de dos poblaciones
marcas = ["Ford", "Toyota", "Chevrolet"]
resultado_mas_dos_poblaciones, f_stat, p_value_mas = prueba_hipotesis_mas_dos_poblaciones(df, marcas)
print(f"Resultado prueba más de dos poblaciones: {resultado_mas_dos_poblaciones}, F-stat: {f_stat:.4f}, p-value: {p_value_mas:.4f}")