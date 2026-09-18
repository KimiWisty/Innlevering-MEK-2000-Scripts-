# Importerer biblioteker
import matplotlib.pyplot as plt
import numpy as np

# Laster inn data direkte fra fila i samme mappe
data = np.loadtxt("Datasett.dat")
x_vektor = data[:, 0]
y_vektor = data[:, 1]

# Lineær regresjon med minste kvadraters metode (grad 1)
# a er stigningstall (beta), b er skjæringspunkt (alpha)
a, b = np.polyfit(x_vektor, y_vektor, 1)

# Genererer y-verdier for regresjonslinjen: y = a*x + b
y_reg = a * x_vektor + b

# Lager plottet med punkter og regresjonslinje
plt.figure(1)
plt.clf()

# Plotter datapunktene
plt.plot(x_vektor, y_vektor, "o", color="black", label="Datapunkter")

# Plotter regresjonslinjen
plt.plot(x_vektor, y_reg, color="red", linewidth=2, label=f"Tilpasning: y = {b:.2f} + {a:.2f}x")

# Navn på aksene
plt.xlabel("x", fontsize=22)
plt.ylabel("y", fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(True)
plt.legend(fontsize=14)  # Viser forklaring på linje/punkter

plt.tight_layout()
plt.show()

# Skriver ut resultatene i terminalen
print(f"Skjæringspunkt (alpha): {b:.4f}")
print(f"Stigningstall (beta):   {a:.4f}")