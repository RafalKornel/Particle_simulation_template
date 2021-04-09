from matplotlib import pyplot as plt
from matplotlib import animation

from .simulator import Simulator


def visualize(simulator: Simulator) -> None:
    ''' 
    Basic visualization function. When invoked, will run animation, untill 
    program is working. Argument (simulator) should be an object containing 2 properties:
        -particles: a field containing array of objects, that have x and y properties,
        -evolve: a function that calculates one step of simulation.
    '''

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        simulator.evolve()

        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return line,

    anim = animation.FuncAnimation(
        fig, animate, init_func=init, blit=True, interval=10)

    plt.show()
