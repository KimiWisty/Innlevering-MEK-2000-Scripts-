import matplotlib.pyplot as plt
import numpy as np

# Importerer de ferdige parametrene fra forrige oppgave e)
from Oppgave_e import a, b, c, d, f

# Laster inn måledata
data = np.loadtxt("Datasett.dat")
x_vektor = data[:, 0]
y_vektor = data[:, 1]

x_slutt = 6 #Vi vet vi vil ha verdien til x = 5 så for å gjøre det mer oversiktlig setter vi figurens max x verdi til 6
# Genererer en tett/glatt x-akse for linjene
x_modell = np.linspace(min(x_vektor), x_slutt, 1000) 

# Beregner den lineære regresjonslinjen og den fulle modellen F(x)
y_regresjon = a + b * x_modell
y_modell = a + b * x_modell + c * np.sin(d * x_modell + f)

# beregner verdien til x = 5
x_val = 5
y_val = a + b * x_val + c * np.sin(d * x_val + f)


# Lager plottet med alle tre elementene sammen
plt.figure(1)
plt.clf()

# Datapunktene fra oppgave a
plt.plot(x_vektor, y_vektor, "o", color="black", label="Måledata")

# Lineær regresjonslinje (a + bx)
plt.plot(
    x_modell,
    y_regresjon,
    "--",
    color="blue",
    linewidth=2,
    label="Regresjonslinje ($a + bx$)",
)

# Den fulle modellen F(x)
plt.plot(
    x_modell,
    y_modell,
    "-",
    color="red",
    linewidth=2,
    label="Full modell $F(x)$",
)

# Markering av x = 5 ---
# Plotter et uthevet punkt i (5, y_5)
plt.plot(x_val, y_val, "*", color="green", markersize=14, label=f"F(5) = {y_val:.2f}")

# Hjelpelinjer fra aksene til punktet
plt.axvline(x=x_val, color="gray", linestyle=":", linewidth=1.5)
plt.axhline(y=y_val, color="gray", linestyle=":", linewidth=1.5)

# Tekstforklaring direkte ved punktet
plt.annotate(
    f"  x=5, y={y_val:.2f}",
    xy=(x_val, y_val),
    fontsize=14,
    fontweight="bold",
    color="green",
    verticalalignment="bottom",
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