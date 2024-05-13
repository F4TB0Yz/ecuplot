import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Geogebra:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_geogebra(self):
        self.driver.get('https://www.geogebra.org/calculator')
        time.sleep(2)
        self.input_funcion = self.driver.find_element(By.XPATH, '//*[@class="gwt-Label avDummyLabel"]')
        self.input_funcion.click()
        self.input_funcion.send_keys('x^2 + 5x + 6')
        time.sleep(5)

    def obtenerFuncion(self):
        ...
        

Geogebra().get_geogebra()
