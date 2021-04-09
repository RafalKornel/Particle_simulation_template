from src.visualize import visualize
from src.particle import Particle
from src.simulator import Simulator


def test_visualize() -> None:
    particles = [Particle(0.3, 0.5),
                 Particle(0.0, -0.5),
                 Particle(-0.1, -0.4)]
    simulator = Simulator(particles)
    visualize(simulator)
