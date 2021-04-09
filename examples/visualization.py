from src.visualize import visualize
from src.particle import Particle
from src.simulator import Simulator


def test_visualize():
    particles = [Particle(0.3, 0.5, +1),
                 Particle(0.0, -0.5, -1),
                 Particle(-0.1, -0.4, +3)]
    simulator = Simulator(particles)
    visualize(simulator)
