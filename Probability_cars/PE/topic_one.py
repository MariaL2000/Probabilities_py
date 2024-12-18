import pandas as pd

def probabilidad_coche_usa(df):
    """Calcula la probabilidad de que un coche provenga de USA."""
    total_vehiculos = len(df)
    vehiculos_usa = len(df[df['origin'] == 'usa'])
    probabilidad = vehiculos_usa / total_vehiculos
    return probabilidad

def probabilidad_volvo_europa(df):
    """Calcula la probabilidad de que un coche provenga de Europa y sea un Volvo."""
    total_vehiculos_europa = len(df[df['origin'] == 'europe'])
    vehiculos_volvo_europa = len(df[(df['origin'] == 'europe') & (df['name'].str.contains('volvo', case=False))])
    if total_vehiculos_europa > 0:
        probabilidad = vehiculos_volvo_europa / total_vehiculos_europa
    else:
        probabilidad = 0
    return probabilidad


def probabilidad_horsepower_usa(df):
    """Calcula la probabilidad de que un coche tenga un horsepower >= 220 dado que proviene de USA usando Bayes."""
    
    # Total de vehículos
    total_vehiculos = len(df)
    
    # Total de vehículos que provienen de USA
    vehiculos_usa = len(df[df['origin'] == 'usa'])
    
    # Total de vehículos con horsepower >= 220
    vehiculos_horsepower_220 = len(df[df['horsepower'] >= 220])
    
    # Total de vehículos que provienen de USA y tienen horsepower >= 220
    vehiculos_horsepower_220_usa = len(df[(df['origin'] == 'usa') & (df['horsepower'] >= 220)])
    
    # Probabilidad P(A) = P(horsepower >= 220)
    if total_vehiculos > 0:
        prob_horsepower = vehiculos_horsepower_220 / total_vehiculos
    else:
        prob_horsepower = 0
    
    # Probabilidad P(B) = P(usa)
    if total_vehiculos > 0:
        prob_usa = vehiculos_usa / total_vehiculos
    else:
        prob_usa = 0
    
    # Probabilidad P(B|A) = P(usa | horsepower >= 220)
    if vehiculos_horsepower_220 > 0:
        prob_usa_given_horsepower = vehiculos_horsepower_220_usa / vehiculos_horsepower_220
    else:
        prob_usa_given_horsepower = 0
    
    # Aplicar la fórmula de Bayes
    if prob_horsepower > 0:
        probabilidad = (prob_usa_given_horsepower * prob_usa) / prob_horsepower
    else:
        probabilidad = 0
    
    return probabilidad