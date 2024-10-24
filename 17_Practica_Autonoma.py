import matplotlib.pyplot as plt
import pandas as pd

#diccionario de datos 
data = {
    'Ciudad': ['Acapulco', 'Acapulco', 'Acapulco', 'Monterrey', 'Monterrey', 'Monterrey', 'Guadalajara', 'Guadalajara', 'Guadalajara'],
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo'],
    'Temperatura': [25, 28, 30, 15, 18, 22, 18, 20, 25]
}

#hacemos un Dataframe de pandas con los datos proporcionados
df = pd.DataFrame(data)

#calcular la terperatura media de cada ciudad 
temperatura_media = df.groupby('Ciudad')['Temperatura'].mean() #df.groupby('Ciudad'): Agrupa los datos del DataFrame por la columna 'Ciudad'.
#['Temperatura']: Selecciona la columna 'Temperatura' dentro de cada grupo (ciudad). #.mean(): Calcula la media (promedio) de las temperaturas para cada ciudad.

#funcion lambda que convierta las tem de grados Celsius a grados Faherheit
df['Temperatura_F'] = df['Temperatura'].apply(lambda c: (c * 9/5) + 32)

# Calcular la temperatura media en Fahrenheit de cada ciudad
temperatura_media_fahrenheit = df.groupby('Ciudad')['Temperatura_F'].mean()

# Función para crear un gráfico de líneas con las temperaturas mensuales de una ciudad
def graficar_temperaturas(df, ciudad, titulo="Temperaturas Mensuales", etiqueta_x="Mes", etiqueta_y="Temperatura (°C)", color="blue"):
    # Filtrar el DataFrame para que solo tenga los datos de la ciudad seleccionada
    df_ciudad = df[df['Ciudad'] == ciudad]
    
    # Crear el gráfico de líneas
    plt.plot(df_ciudad['Mes'], df_ciudad['Temperatura'], color=color, marker='o', linestyle='-', label=f'{ciudad}')
    
    # Personalizar el gráfico
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    
    # Mostrar leyenda
    plt.legend()
    
    # Mostrar el gráfico
    plt.show()
    
# Llamada a la función para mostrar el gráfico de Acapulco con personalización 
# llama cada funcion con el nombre de la ciudad que quieres ver
graficar_temperaturas(df, 'Acapulco', titulo="Temperaturas en Acapulco", etiqueta_x="Meses", etiqueta_y="Temperatura en °C", color="red")
graficar_temperaturas(df, 'Monterrey', titulo="Temperaturas en Monterrey", etiqueta_x="Meses", etiqueta_y="Temperatura en °C", color="blue")
graficar_temperaturas(df, 'Guadalajara', titulo="Temperaturas en Guadalajara", etiqueta_x="Meses", etiqueta_y="Temperatura en °C", color="black")
