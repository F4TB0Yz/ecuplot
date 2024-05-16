import sys

from matplotlib import pyplot

class Graficador:
    def __init__(self):
        self.rango = range(-10, 15)

    def funcion_1(self, x, funcion):
        return eval(funcion)
    
    def funcion_2(self, x, funcion):
        return funcion.replace("x", str(x))
    
    def graficar(self, *args):
        pyplot.plot(self.rango, [self.funcion_1(i, '3*x**3 - 2*x**2 + 3*x - 1') for i in self.rango])
        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")
        pyplot.xlim(-10, 10)
        pyplot.ylim(-10, 10)
        pyplot.savefig("output.png")
        pyplot.show()

Graficador().graficar()