> forked from [xhinker](https://github.com/xhinker)/[orbit](https://github.com/xhinker/orbit)

# Simulate Flyby in Python
This project tries to calculate a simple orbit of e.g. a space probe that depends from several planets. The positions of the planets are fetched as Ephemeris from NASA's [Horizon system](https://ssd.jpl.nasa.gov/horizons/), the Space Probe is calculated with the [Euler-Cromer method](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method).

### Contents:
The repo contains multiple files:
1. `solar-system-plt.py`, which only uses the Ephemeris to plot the orbits with pyplot.
![solar system](images/Screenshot%20from%202022-12-22%2018-23-18.png)

2. `flyby.py`, where the solar system is animated with a space probe that makes a flyby around venus.
![flyby](images/Screen-Recording-2022-12-22-at-1.gif)
