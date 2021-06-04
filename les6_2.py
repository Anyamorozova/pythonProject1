class Road:
    
    _length = None
    _width = None

    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def massa(self, asphalt, thickness):
        return self._length * self._width * asphalt * thickness
        
road = Road(20,5000)
print(road.massa(25,5))
