import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Definir las etiquetas de los conjuntos
labels = {'100': 'Etnia', 
          '010': 'Raza', 
          '001': 'Cultura', 
          '110': 'Etnia y Raza', 
          '101': 'Etnia y Cultura', 
          '011': 'Raza y Cultura', 
          '111': 'Etnia, Raza y Cultura'}

# Crear el diagrama de Venn
plt.figure(figsize=(10, 8))
venn = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=('Etnia', 'Raza', 'Cultura'))

# Añadir las etiquetas a los subconjuntos
for subset in labels:
    venn.get_label_by_id(subset).set_text(labels[subset])

plt.title('Diagrama de Venn de Etnia, Raza y Cultura')
plt.show()