import matplotlib.pyplot as plt

# Definir los puntos
P1 = (1, 3)
P2 = (11, 5)
P3 = (7, -1)
P4 = (-3, -3)

# Crear la figura y el eje
fig, ax = plt.subplots()

# Dibujar el paralelogramo
x_values = [P1[0], P2[0], P3[0], P4[0], P1[0]]
y_values = [P1[1], P2[1], P3[1], P4[1], P1[1]]
ax.plot(x_values, y_values, marker='o')

# Anotar los puntos
ax.text(P1[0], P1[1], 'P1(1, 3)', fontsize=12, ha='right')
ax.text(P2[0], P2[1], 'P2(11, 5)', fontsize=12, ha='right')
ax.text(P3[0], P3[1], 'P3(7, -1)', fontsize=12, ha='right')
ax.text(P4[0], P4[1], 'P4(-3, -3)', fontsize=12, ha='right')

# Configurar los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Figura de la fábrica')
ax.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Mostrar la gráfica
plt.show()
