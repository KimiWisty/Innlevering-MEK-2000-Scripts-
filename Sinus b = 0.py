import matplotlib.pyplot as plt
import numpy as np

# 1. Henter datasettet for å finne området for x-aksen
data = np.loadtxt("Datasett.dat")
x_data = data[:, 0]
y_data = data[:, 1]

# Setter inn parameter verdier. Her setter jeg b = 0 for å vise hvordan funksjonen som er bra for klimaet vil se ut. 
# Dersom vi vil ha en minkende gasskonsentrasjon så hadde b < 0 vært ideellt. Om det er realistisk er en annen historie. 
a = 406.9177
b = 0
c = 2.7820
d = 6.2960
f = -0.6091


# Definerer funksjonen F(x)
def F(x, a, b, c, d, f):
    return a + b * x + c * np.sin(d * x + f)


x_modell = np.linspace(min(x_data), max(x_data), 1000)

#Regner ut y-verdiene til F(x)
y_modell = F(x_modell, a, b, c, d, f)

#Plotting
plt.figure(figsize=(10, 6))

#Tegner måledataene som svarte punkter
plt.plot(x_data, y_data, "o", color="black", label="Måledata")

# Tegner funksjonen F(x) som en rød linje
plt.plot(
    x_modell,
    y_modell,
    "-",
    color="red",
    linewidth=2,
    label="$F(x) = a + bx + c\sin(dx + f)$",
)

# Styling
plt.xlabel("x", fontsize=18)
plt.ylabel("y", fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True)
plt.legend(fontsize=14)
plt.tight_layout()

plt.show()