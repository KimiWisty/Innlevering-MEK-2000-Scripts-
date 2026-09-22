import numpy as np

# Henter datasettet
data = np.loadtxt("Datasett.dat")

# Henter ut alle rader (:) fra henholdsvis første (0) og andre (1) kolonne
x_data = data[:, 0]
y_data = data[:, 1]

a_0 = 407.09
b_0 = 2.87
c_0 = 1.0
d_0 = 1.0
f_0 = 1.0
h = 0.0001


# Definerer summen av de kvadratiske avvikene S(a, b, c, d, f)
def S(a, b, c, d, f, x_data, y_data):
    # Modellfunksjonen fra oppgaven: F(x) = a + b*x + c*sin(d*x + f)
    y_modell = a + b * x_data + c * np.sin(d * x_data + f)

    # Regner ut summen fra i=1 til n for (y_i - F(x_i))^2
    return np.sum((y_data - y_modell) ** 2)


# Regner ut verdiene
S_0 = S(a_0, b_0, c_0, d_0, f_0, x_data, y_data)
S_1 = S(a_0 + 0.0001, b_0, c_0, d_0, f_0, x_data, y_data)
S_2 = S(a_0 - 0.0001, b_0, c_0, d_0, f_0, x_data, y_data)

a_1 = a_0 + h
a_2 = a_0 - h

# Skriver ut resultane for S1, S2 og S med originale verdier
print(f"S_1(a + h, b, c, d, f) = {S_1:.5f}")
print(f"S_2(a - h, b, c, d, f) = {S_2:.5f}")
print(f"S_0(a, b, c, d, f) = {S_0:.5f}")