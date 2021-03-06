class Particle:
    ''' Basic data structure for single particle entity. '''

    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
