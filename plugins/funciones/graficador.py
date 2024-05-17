import numpy as np
from matplotlib import pyplot

class Graficador:
    def __init__(self):
        self.rango = range(-11, 15)

    def funcion(self, x, funcion):
        funcion_adaptada = funcion.replace('x', str(x))
        print(f'{funcion_adaptada}: {eval(funcion_adaptada)}')
        return eval(funcion_adaptada)
    
    def graficar(self, *args):
        for i in range(len(args)):
            print(i)
            pyplot.plot(self.rango, [self.funcion(j + 1, args[i]) for j in self.rango])
        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")
        pyplot.xlim(-10, 10)
        pyplot.ylim(-10, 10)
        pyplot.savefig("output.png")