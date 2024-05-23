import math

import numpy as np
from matplotlib import pyplot

class Graficador:
    def __init__(self):
        self.rango = range(-11, 15)
        self.funcion_valida = True

    def funcionEval(self, x, funcion):
        print(f'funcion: {funcion}')
        if 'np.sqrt' in funcion:
            funcion_adaptada = funcion.replace('x', f'({str(x)})')
            print(eval(funcion_adaptada))
            if math.isnan(eval(funcion_adaptada)):
                self.funcion_valida = False
                return 0
        else:
            funcion_adaptada = funcion.replace('x', f'({str(x)})')
        print(funcion_adaptada)
        print(f'{funcion_adaptada}: {eval(funcion_adaptada)}')
        return eval(funcion_adaptada)
    
    def graficar(self, *args):
        pyplot.clf()  # Limpia la figura actual 
        for i in range(len(args)):
            pyplot.plot(self.rango, [self.funcionEval(j, args[i]) for j in self.rango])
        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")
        pyplot.xlim(-10, 10)
        pyplot.ylim(-10, 10)
        pyplot.savefig("output.png")