from src.simulator import Simulator
from src.utilities import with_timer


def run_benchmark():
    benchmark_with_timer, get_time, times = with_timer(benchmark, 5)
    benchmark_with_timer()
    print(f"Total time of benchmark: {get_time() / 1000} s.")
    print("Array of run times (in ms):\n", times)


def benchmark():
    simulator = Simulator()
    simulator.evolve()
