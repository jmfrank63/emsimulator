# A simple electric field function in pure python

from math import sqrt

EMC = 1.60217662E-19

class ChargedParticle:
    def __init__(self, position, charge=-EMC):
        self.position = position
        self.charge = charge

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def charge(self):
        return self.__charge

    @charge.setter
    def charge(self, value):
        self.__charge = value

    def distance_to(self, point=(0,0,0)):
        return sqrt(self.position[0] * self.position[0] + \
                    self.position[1] * self.position[1] + \
                    self.position[2] * self.position[2])

    def field_at(self, point=(0,0,0)):
        pass
    
def potential(probe, pointarray):
    pass

e = ChargedParticle([0,0,0])
p = ChargedParticle((1,1,1), EMC)

print(p.position)
print(e.position)

print(e.distance_to((0,0,0)))
print(p.distance_to((0,0,0)))
