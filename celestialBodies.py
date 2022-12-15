from __future__ import annotations
from astroquery.jplhorizons import Horizons

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
        self.x   = [ a * self.AU2meters for a in eph['x'] ]
        self.y   = [ b * self.AU2meters for b in eph['y'] ]
        self.z   = [ c * self.AU2meters for c in eph['z'] ]

    def __init__(self, name, num, start="2010-01-01", stop="2030-01-01"):
        self.name = name
        self.id = num
        self.start = start
        self.stop = stop
        self.getVectors()

class spaceProbe:
    def __init__(self):
        pass