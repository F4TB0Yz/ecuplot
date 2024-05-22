import os

from pyrogram import Client, filters
from plugins.funciones.graficador import Graficador

@Client.on_message(filters.command(['graficar'], ['!','.','/']))
async def startComando(client, message):
    user_name = message.from_user.username
    user_id = message.from_user.id

    mensaje_usuario = message.text[len('/graficar'):]
    mensaje = await filtrarMensaje(mensaje_usuario)
    graficador = Graficador()
    graficador.graficar(*mensaje)


    return await message.reply_photo('output.png')


async def filtrarMensaje(mensaje):
    print(type(mensaje))
    mensaje = [funcion.replace(' ', '') for funcion in mensaje]

    mensaje_nuevo = ""
    for index, caracter in enumerate(mensaje):
        if caracter.isdigit() and index + 1 < len(mensaje) and mensaje[index + 1] == 'x':  # Evitar IndexErrors
            mensaje_nuevo += caracter + "*x"
        else:
            mensaje_nuevo += caracter
    if '&' in mensaje_nuevo:
        mensaje_nuevo = [funcion.split('&') for funcion in mensaje_nuevo]
    mensaje_nuevo = [funcion.replace(' ', '') for funcion in mensaje_nuevo]
    mensaje_nuevo = [funcion.replace('^', '**') for funcion in mensaje_nuevo]
    mensaje_nuevo = [funcion.replace('sqrt', 'np.sqrt') for funcion in mensaje_nuevo]
    #mensaje = [funcion.replace('+*', '+') for funcion in mensaje]
    print(type(mensaje_nuevo))
    return mensaje_nuevo

async def borrarImg():
    os.remove('output.png')
