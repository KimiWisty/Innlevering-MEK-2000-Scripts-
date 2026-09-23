# Dette regner ut gjennomsnittet av x og gjennomsnitet av y
# For MKM
# Importerer bibliotek
import numpy as np
import statistics

# Laster inn data direkte fra fila i samme mappe
data = np.loadtxt("Datasett.dat")
x_vektor = data[:, 0]
y_vektor = data[:, 1]

# Regner ut gjennomsnittet for x og y
x_avg = statistics.mean(x_vektor)
y_avg = statistics.mean(y_vektor)

print("x_avg =", x_avg)
print("y_avg =", y_avg)