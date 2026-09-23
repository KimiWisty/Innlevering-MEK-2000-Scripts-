import matplotlib.pyplot as plt
import numpy as np

# Importerer de ferdige parameteren fra forrige oppgave e)
from Oppgave_e import a, b, c, d, f

# Laster inn måledata
data = np.loadtxt("Datasett.dat")
x_vektor = data[:, 0]
y_vektor = data[:, 1]

# Genererer en tett/glatt x-akse for linjene
x_modell = np.linspace(min(x_vektor), max(x_vektor), 1000)

# Beregner den lineære regresjonslinjen og den fulle modellen F(x)
y_regresjon = a + b * x_modell
y_modell = a + b * x_modell + c * np.sin(d * x_modell + f)

# Lager plottet med alle tre elementene sammen
plt.figure(1)
plt.clf()

# 1. Datapunktene fra oppgave a
plt.plot(x_vektor, y_vektor, "o", color="black", label="Måledata")

# 2. Lineær regresjonslinje (a + bx)
plt.plot(
    x_modell,
    y_regresjon,
    "--",
    color="blue",
    linewidth=2,
    label="Regresjonslinje ($a + bx$)",
)

# 3. Den fulle modellen F(x)
plt.plot(
    x_modell,
    y_modell,
    "-",
    color="red",
    linewidth=2,
    label="Full modell $F(x)$",
)

# Styling og skriftstørrelser
plt.xlabel("x", fontsize=22)
plt.ylabel("y", fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=14)
plt.grid(True)

plt.tight_layout()
plt.show()