from src.simulator import Simulator
from src.utilities import with_timer

def benchmark():
    def runner():
        simulator = Simulator()
        simulator.evolve(dt=0.1)

    runner_with_timer, times = with_timer(runner, 10)
    runner_with_timer()
    print(f"Total time of benchmark: {sum(times) / 1000} s.")
    print(f"Average time of single benchmark: {sum(times)/len(times)} ms")
    print("Array of run times (in ms):\n", times)


def benchmark_memory():
    simulator = Simulator(particle_count=100000)
    simulator.evolve(dt=0.0001)
