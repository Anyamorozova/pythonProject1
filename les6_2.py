class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def massa(self, asphalt, thickness):
        return self._length * self._width * asphalt * thickness
        
road = Road(100,100)
print(road.massa(2,3))
