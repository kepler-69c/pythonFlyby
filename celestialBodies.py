from __future__ import annotations
from astroquery.jplhorizons import Horizons
from data import *

class planet:
    AU2meters: int = 149597870700
    step: str = "1d"
    start: str
    stop: str

    def __str__(self):
        return f"{self.name} with ID {self.id}"

    def getVectors(self):
        obj = Horizons( id=self.id, location=None, epochs={'start':self.start, 'stop':self.stop, 'step':self.step})
        # obj = Horizons(id=self.planet, location=self.id, epochs={'start':'2010-01-01', 'stop':'2030-01-01', 'step':'1d'})
        eph = obj.vectors()
        # print(eph)
        self.x   = [ a * self.AU2meters for a in eph['x'] ]
        self.y   = [ b * self.AU2meters for b in eph['y'] ]
        self.z   = [ c * self.AU2meters for c in eph['z'] ]
        self.vx  = [ d * self.AU2meters for d in eph["vx"]]
        self.vy  = [ e * self.AU2meters for e in eph["vy"]]
        self.vz  = [ f * self.AU2meters for f in eph["vz"]]
        self.d   = [ g.split(" ")[1] for g in eph["datetime_str"]]

    def __init__(self, name, num, start="2010-01-01", stop="2030-01-01"):
        self.name = name
        self.id = num
        self.start = start
        self.stop = stop
        self.getVectors()

class spaceProbe:
    AU2meters: int = 149597870700
    xv, yv, zv = 0,0,0
    xlist,ylist,zlist = [],[],[]
    c = 0
    dt = 24*3600

    def computeGravity(self):
        gravconst = G*Ms*self.mass
        # compute G force
        rx,ry,rz = self.x/self.AU2meters - self.sun.x[self.c], self.y/self.AU2meters - self.sun.y[self.c], self.z/self.AU2meters - self.sun.z[self.c]
        if self.c < 3:
            print(self.x/1E11)
            print(rx/1E11)
        modr3 = (rx**2+ry**2+rz**2)**1.5
        fx = -gravconst*rx/modr3
        fy = -gravconst*ry/modr3
        fz = -gravconst*rz/modr3
        
        # update quantities how is this calculated?  F = ma -> a = F/m
        self.xv += fx*self.dt/self.mass
        self.yv += fy*self.dt/self.mass
        self.zv += fz*self.dt/self.mass
        
        # update position
        self.x += self.xv*self.dt
        self.y += self.yv*self.dt 
        self.z += self.zv*self.dt

        self.xlist.append(self.x)
        self.ylist.append(self.y)
        self.zlist.append(self.z)

        self.c += 1

    def __init__(self, mass, sun, venus, earth, mars, timestep):
        self.sun = sun
        self.venus = venus
        self.mars = mars

        self.earth = earth
        self.x = self.earth.x[0]
        self.y = self.earth.y[0]
        self.z = self.earth.z[0]
        self.xv = self.earth.vx[0]
        self.yv = self.earth.vy[0]
        self.zv = self.earth.vz[0]

        self.mass = mass
        if timestep == "1d":
            print(self.x/1E11)
            print(timestep)
            self.dt = 1*daysec # every frame move this time
        for i in range(len(earth.x)):
            self.computeGravity()