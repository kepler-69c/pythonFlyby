from astroquery.jplhorizons import Horizons

class planet:
    AU2meters: int = 149597870700

    def __str__(self):
        return f"{self.planet} with ID {self.id}"

    def getVectors(self):
        obj = Horizons( id=self.id, id_type='majorbody', location=None, epochs={'start':'2010-01-01', 'stop':'2030-01-01', 'step':'1d'})
        # obj = Horizons(id=self.planet, location=self.id, epochs={'start':'2010-01-01', 'stop':'2030-01-01', 'step':'1d'})
        eph = obj.vectors()
        self.x   = [ a * self.AU2meters for a in eph['x'] ]
        self.y   = [ b * self.AU2meters for b in eph['y'] ]
        self.z   = [ c * self.AU2meters for c in eph['z'] ]

    def __init__(self, planet, num):
        self.planet = planet
        self.id = num
        self.getVectors()

venus = planet("Venus", 299)
earth = planet("Earth", 399)
mars = planet("Mars", 499)

print(f"{venus}\n{earth}\n{mars}")
#ceres = planet("Ceres", 568)
#print(ceres)