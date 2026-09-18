# Importerer biblioteker
import matplotlib.pyplot as plt
import numpy as np

# Laster inn data direkte fra fila i samme mappe
data = np.loadtxt("Datasett.dat")
x_vektor = data[:, 0]
y_vektor = data[:, 1]

# Lager plottet med punkter
plt.figure(1)
plt.clf()

plt.plot(x_vektor, y_vektor, "o", color="black")  # 'o' viser individuelle punkter
plt.xlabel("x", fontsize=22) # Gir navn på x-aksen
plt.ylabel("y", fontsize=22) # Gir navn på y-aksen
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(True)

plt.tight_layout()
plt.show()