import math
import random

def Eslope(pm):
    E = []
    slope = []
    for i in range(1000):
        Energy = math.pow(10, 18 + (21 - 18) * (i / 999))
        E.append(Energy)
        if 4.6e18 <= Energy:
            gamma = -3.34 * pm
        if 4.6e18 < Energy <= 5.4e19:
            gamma = -2.67 * pm
        if 5.4e19 < Energy:
            gamma = -4.6 * pm
        else:
            gamma = -2.7 * pm
        slope.append(Energy ** gamma)
    energy = random.choices(E, k=1, weights=slope)
    return energy[0]

def Flux(pm):
    E = Eslope(pm)
    return round(math.log10(E), 1)