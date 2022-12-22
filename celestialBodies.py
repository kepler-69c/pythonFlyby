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

    def __init__(self, name, num, mass, start="2010-01-01", stop="2030-01-01"):
        self.name = name
        self.id = num
        self.mass = mass
        self.start = start
        self.stop = stop
        self.getVectors()

class spaceProbe:
    xv, yv, zv = 0,0,0
    xlist,ylist,zlist = [],[],[]
    c = 0
    dt = 24*3600

    def computeGravity(self, planets, position, c):
        hx, hy, hz = position
        gx, gy, gz = 0,0,0

        for planet in planets:
            gravconst = G*planet.mass*self.mass
            # compute G force
            rx,ry,rz = hx - planet.x[c], hy - planet.y[c], hz - planet.z[c]
            modr3 = (rx**2+ry**2+rz**2)**1.5
            fx = -gravconst*rx/modr3
            fy = -gravconst*ry/modr3
            fz = -gravconst*rz/modr3
        
            gx += fx
            gy += fy
            gz += fz         

        # update quantities how is this calculated?  F = ma -> a = F/m
        self.xv += gx*self.dt/self.mass
        self.yv += gy*self.dt/self.mass
        self.zv += gz*self.dt/self.mass
        
        # update position
        hx += self.xv*self.dt
        hy += self.yv*self.dt 
        hz += self.zv*self.dt

        return hx,hy,hz

    def __init__(self, mass, sun, venus, earth, mars, timestep, velocity=1):
        self.earth = earth
        self.x = self.earth.x[0]
        self.y = self.earth.y[0]
        self.z = self.earth.z[0]
        self.xv = self.earth.vx[0]/timestep * velocity
        self.yv = self.earth.vy[0]/timestep * velocity
        self.zv = self.earth.vz[0]/timestep * velocity

        self.mass = mass
        self.dt = timestep # every frame move this time

        for i in range(len(earth.x)):
            x, y, z = self.computeGravity([sun, venus, mars], [self.x, self.y, self.z], self.c)
            self.c += 1

            self.x, self.y, self.z = x, y, z
            self.xlist.append(x)
            self.ylist.append(y)
            self.zlist.append(z)