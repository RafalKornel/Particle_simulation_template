from .particle import Particle


class Simulator:
    ''' 
    Class responsible for running simulation. Should contain particles
    field, and evolve function. Make it unaware of Particle initial implementation,
    as well as visualization concern. Only simulation logic here.
    '''

    def __init__(self, particles: list[Particle] or None = None):
        ''' Particles is array of objects. '''
        self.particles = particles or self.initialize_particles()

    def initialize_particles(self) -> list[Particle]:
        ''' Setting up initial particles. '''
        return []

    def evolve(self, dt: float = 0.1) -> None:
        ''' Main function, should calculate one step of simulation. '''
        pass
