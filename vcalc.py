# A program that calculates velocity and ToF from mass and energy
import math
# E = mv^2/2
# Run	p 0.577 MeV	p 1.815 MeV	α 1.4 MeV	α 1.464 MeV	α 2.05 MeV	α 4.75 MeV	3H 2.73 MeV

V = []
T = []
E = [0.577, 1.815, 1.4, 1.464, 2.05, 4.75, 2.73] #MeV
m = [938.27, 938.27, 3728.4, 3728.4, 3728.4, 3728.4, 2809.41] # MeV
c = 3*10**8
s = 36.15 #mm

for i in range(len(E)):
    v = math.sqrt(2*E[i]/m[i])*c
    V.append(round(v,2))

    t = (s*10**-3)/v
    T.append(t)

print(V)
print(T)