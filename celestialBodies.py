from __future__ import annotations
from astroquery.jplhorizons import Horizons
from data import *

# Klasse für die Planeten
class planet:
    AU2meters: int = 149597870700
    step: str = "1d"
    start: str
    stop: str

    def __str__(self):
        return f"{self.name} with ID {self.id}"

	# Einspeichern der Ephemeriden als Vektoren aus dem Horizon System der NASA
    def getVectors(self):
        obj = Horizons( id=self.id, location=None, epochs={'start':self.start, 'stop':self.stop, 'step':self.step})
        eph = obj.vectors()
        self.x   = [ a * self.AU2meters for a in eph['x'] ]
        self.y   = [ b * self.AU2meters for b in eph['y'] ]
        self.z   = [ c * self.AU2meters for c in eph['z'] ]
        self.vx  = [ d * self.AU2meters for d in eph["vx"]]
        self.vy  = [ e * self.AU2meters for e in eph["vy"]]
        self.vz  = [ f * self.AU2meters for f in eph["vz"]]
        self.d   = [ g.split(" ")[1] for g in eph["datetime_str"]]

	# Initialisierung
    def __init__(self, name, num, mass, start="2010-01-01", stop="2030-01-01"):
        self.name = name
        self.id = num
        self.mass = mass
        self.start = start
        self.stop = stop
        self.getVectors()

# Klasse für die Probe
class spaceProbe:
    xv, yv, zv = 0,0,0
    xlist,ylist,zlist = [],[],[]
    c = 0
    dt = 24*3600

	# Euler-Cromer-Verfahren
    def computeGravity(self, planets, position, c):
        hx, hy, hz = position
        fx, fy, fz = 0,0,0

		# Für jeden Himmelskörper wird in jedem Zeitpunkt die Anziehungskraft berechnet...
        for planet in planets:
            gravconst = G*planet.mass*self.mass
            rx,ry,rz = hx - planet.x[c], hy - planet.y[c], hz - planet.z[c]
            modr3 = (rx**2+ry**2+rz**2)**1.5
            fx += -gravconst*rx/modr3
            fy += -gravconst*ry/modr3
            fz += -gravconst*rz/modr3        

        # ...mit der die neue Geschwindigkeit...
        self.xv += fx*self.dt/self.mass
        self.yv += fy*self.dt/self.mass
        self.zv += fz*self.dt/self.mass
        
        # ...und die neue Position berechnet werden
        hx += self.xv*self.dt
        hy += self.yv*self.dt 
        hz += self.zv*self.dt

        return hx,hy,hz

	# initialisierung
    def __init__(self, mass, sun, venus, earth, mars, timestep, velocity=1):
        self.earth = earth
        self.x = self.earth.x[0]
        self.y = self.earth.y[0]
        self.z = self.earth.z[0]
        self.xv = self.earth.vx[0]/timestep * velocity
        self.yv = self.earth.vy[0]/timestep * velocity
        self.zv = self.earth.vz[0]/timestep * velocity

        self.mass = mass
        # jeder Zeitschritt ist so lang
        self.dt = timestep

		# Euler-Cromer-Verfahren
        for i in range(len(earth.x)):
            x, y, z = self.computeGravity([sun, venus, mars], [self.x, self.y, self.z], self.c)
            self.c += 1

            self.x, self.y, self.z = x, y, z
            self.xlist.append(x)
            self.ylist.append(y)
            self.zlist.append(z)
