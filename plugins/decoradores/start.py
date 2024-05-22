from pyrogram.types import InlineKeyboardButton

class DecoradoresStart:
    def __init__(self):
        self.botones = [
                [
                    InlineKeyboardButton(text='Instrucciones', callback_data='instrucciones'),
                    InlineKeyboardButton(text='Acerca de mi', callback_data='acerca')
                ],
                [
                    InlineKeyboardButton(text='Perfil', callback_data='perfil')
                ]
        ]

    def mensajeStart(self, user_name):
        return f"""
Bienvenido **{user_name}!**, Soy **Ecuplot**.

Soy un bot con el que puedes graficar funciones.
Aqui podras encontrar las herramientas con las que cuento!
Nuestro trabajo es mostrar a los usuarios como se ven las funciones mas que graficar por ellos es mostrar como son las funciones, asi como podemos saber como es una funcion cuadratica, es una parabola, una funcion lineal es una recta, una funcion cubica es una curva, una funcion racional es una curva con una asintota, una funcion de raices es una curva con una raiz cuadrada.
Asi pueden guiarse para saber como es una funcion y poder graficarla por si mismos.
Seguiremos trabajando para mejorar y añadir mas funciones, entre ellas resolver ecuaciones paso a paso para asi sea mucho mas eficiente para nuestros usuarios <3.
"""