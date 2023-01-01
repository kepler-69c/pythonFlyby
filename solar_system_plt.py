from astroquery.jplhorizons import Horizons
import matplotlib.pyplot as plt
from celestialBodies import planet, spaceProbe
from data import *
from math import sqrt

start = "2021-11-22"

sun = planet("Sun", 10, Ms, start=start)
venus = planet("Venus", 299, Mv, start=start)
earth = planet("Earth", 399, Me, start=start)
mars = planet("Mars", 499, Mm, start=start)

print(f"{venus}\n{earth}\n{mars}")
#ceres = planet("Ceres", 568)
#print(ceres)

vCurrent = sqrt((earth.vx[0]/daysec)**2 + (earth.vy[0]/daysec)**2 + (earth.vz[0]/daysec)**2)
# vDesired = vCurrent - 4.5E3
vDesired = vCurrent - 3.1E3 # 3100 -> noticing first effect
vPercent = vDesired/vCurrent
print(vCurrent)
print(vDesired)
print(vPercent)

probe = spaceProbe(30, sun, venus, earth, mars, daysec, vPercent)

plt.scatter([0], [0], c="yellow", s=50)
plt.scatter(venus.x, venus.y, c = "brown", s=0.5)
plt.scatter(earth.x, earth.y, c = "blue", s=0.5)
plt.scatter(mars.x, mars.y, c = "red", s=0.5)
plt.scatter(probe.xlist, probe.ylist, c = "red", s=0.1)

# To show the plot
plt.show()