from .particle import Particle
from .utilities import gen


class Simulator:
    def __init__(self, particles=None, grid_size=100, dt=0.01):
        self.grid_size = grid_size
        self.dt = dt
        self.particles = particles or self.initialize_particles()

    def initialize_particles(self, n=100):
        s = self.grid_size
        return [Particle(gen(s), gen(s), gen(5)) for _ in range(n)]

    def evolve(self):
        timestep = 0.0001
        steps = int(self.dt/timestep)

        for i in range(steps):
            for p in self.particles:

                norm = (p.x**2 + p.y**2)**0.5
                v_x = (-p.y)/norm
                v_y = p.x/norm

                d_x = timestep * p.omega * v_x
                d_y = timestep * p.omega * v_y

                p.x += d_x
                p.y += d_y
