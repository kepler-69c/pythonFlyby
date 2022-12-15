from astroquery.jplhorizons import Horizons
import matplotlib.pyplot as plt
from celestialBodies import planet

venus = planet("Venus", 299)
earth = planet("Earth", 399)
mars = planet("Mars", 499)

print(f"{venus}\n{earth}\n{mars}")
#ceres = planet("Ceres", 568)
#print(ceres)

plt.scatter([0], [0], c="yellow", s=50)
plt.scatter(venus.x, venus.y, c = "brown", s=0.5)
plt.scatter(earth.x, earth.y, c = "blue", s=0.5)
plt.scatter(mars.x, mars.y, c = "red", s=0.5)
 
# To show the plot
plt.show()