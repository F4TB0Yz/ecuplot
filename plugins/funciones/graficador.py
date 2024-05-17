import numpy as np
from matplotlib import pyplot

class Graficador:
    def __init__(self):
        self.rango = range(-10, 15)

    def funcion(self, x, funcion):
        funcion = funcion.replace('x', str(x))
        print(f'argumento funcion: {funcion}')
        return eval(funcion)
    
    def graficar(self, *args):
        for i in range(len(args)):
            pyplot.plot(self.rango, [self.funcion(j, args[i]) for j in self.rango])
        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")
        pyplot.xlim(-10, 10)
        pyplot.ylim(-10, 10)
        pyplot.savefig("output.png")