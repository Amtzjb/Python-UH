import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [5, 6, 7, 8], color = 'red' , label = 'serie 1', linestyle = ':', marker = 'D')  # Datos para el eje x y el eje y
plt.plot([4, 5, 7, 9], [2, 7, 4, 6], label = 'serie 2' 'b--*')
plt.legend()
plt.xlabel("Eje X")  # Etiqueta del eje x
plt.ylabel("Eje Y")  # Etiqueta del eje y
plt.title("Gráfico de Líneas")  # Título del gráfico
plt.show()  # Mostrar el gráfico


