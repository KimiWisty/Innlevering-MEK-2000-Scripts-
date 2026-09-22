#Oppgave e) Gradient metoden

# importerer bibliotek
import matplotlib.pyplot as plt
import numpy as np

# Henter datasettet fra oppgaven
data = np.loadtxt("Datasett.dat")

# Henter ut rader fra datasettet
x_data = data[:, 0]
y_data = data[:, 1]

# Velger start sett for parameterene a, b, c, d, f.
# Setter a_0 og b_0 lik parameterene alpha og beta fra lineær regresjon 
# Prøver med intelligent gjetting
a = 407.09 # Konstantleddet
b = 2.87 # Stigningstallet fra den lineære regresjonen
c = 3 # Representerer høyden av svingingene (Amplitude). Et lite, fornuftig tall som 3 gir et OK utgangspunkt
d = 2*np.pi # Antar periode er T = 1 år så det vil si d = 2*pi
f = 0 # Faseforskyvning settes til 0 som et nøytralt utgangspunkt. 

# Parametre for gradient metoden
lærinsrate = 0.0001
h = 0.0001
antall_iterasjoner = 20000


# Definerer en funksjon med 5 variabler
def S(a, b, c, d, f):
    # Modellfunksjonen: S(x) = a + b*x + c*sin(d*x + f)
    y_modell = a + b * x_data + c * np.sin(d * x_data + f)
    # Regner ut summen av de kvadratiske avvikene
    return np.sum((y_modell - y_data) ** 2)

# Midtpunktsformelen for å regne ut partiell deriverte 
def dS_da(a, b, c, d, f):
    return (S(a + h, b, c, d, f) - S(a - h, b, c, d, f)) / (2 * h)


def dS_db(a, b, c, d, f):
    return (S(a, b + h, c, d, f) - S(a, b - h, c, d, f)) / (2 * h)


def dS_dc(a, b, c, d, f):
    return (S(a, b, c + h, d, f) - S(a, b, c - h, d, f)) / (2 * h)


def dS_dd(a, b, c, d, f):
    return (S(a, b, c, d + h, f) - S(a, b, c, d - h, f)) / (2 * h)


def dS_df(a, b, c, d, f):
    return (S(a, b, c, d, f + h) - S(a, b, c, d, f - h)) / (2 * h)


# Gradientnedstigning (for-løkke)
for i in range(antall_iterasjoner):
    # Regner ut alle stigningstallene (gradientene)
    da = dS_da(a, b, c, d, f)
    db = dS_db(a, b, c, d, f)
    dc = dS_dc(a, b, c, d, f)
    dd = dS_dd(a, b, c, d, f)
    df = dS_df(a, b, c, d, f)

    # Oppdaterer parametrene
    a = a - lærinsrate * da
    b = b - lærinsrate * db
    c = c - lærinsrate * dc
    d = d - lærinsrate * dd
    f = f - lærinsrate * df

    # Skriver ut framgangen underveis
    if i % 1000 == 0:
        print(f"Iterasjon {i}: S = {S(a, b, c, d, f):.4f}")

# Skriv ut de oppnådde verdiene
print("\n--- Optimale parametere ---")
print(
    f"a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, d = {d:.4f}, f = {f:.4f}"
)

# Plotter resultatene til slutten
y_tilpasset = a + b * x_data + c * np.sin(d * x_data + f)
plt.plot(x_data, y_data, "o", label="Måledata")
plt.plot(x_data, y_tilpasset, "-", label="Tilpasset modell F(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()