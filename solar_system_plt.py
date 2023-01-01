from astroquery.jplhorizons import Horizons
import matplotlib.pyplot as plt
from celestialBodies import planet, spaceProbe
from data import *
from math import sqrt

start = "2021-11-22"

# planeten initialisieren
sun = planet("Sun", 10, Ms, start=start)
venus = planet("Venus", 299, Mv, start=start)
earth = planet("Earth", 399, Me, start=start)
mars = planet("Mars", 499, Mm, start=start)

# Anfangsgeschwindigkeit für Sonde Bestimmen: 3183 m/s
vCurrent = sqrt((earth.vx[0]/daysec)**2 + (earth.vy[0]/daysec)**2 + (earth.vz[0]/daysec)**2)
vDesired = vCurrent - 3096 # [m/s] 
vPercent = vDesired/vCurrent

# sonde initialisieren
probe = spaceProbe(30, sun, venus, earth, mars, daysec, vPercent)

# mit pyplot einzeichnen
plt.scatter([0], [0], c="yellow", s=50)
plt.scatter(venus.x, venus.y, c = "brown", s=0.5)
plt.scatter(earth.x, earth.y, c = "blue", s=0.5)
plt.scatter(mars.x, mars.y, c = "red", s=0.5)
plt.scatter(probe.xlist, probe.ylist, c = "red", s=0.1)

plt.show()
