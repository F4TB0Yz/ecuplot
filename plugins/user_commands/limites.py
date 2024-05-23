import os

from pyrogram import Client, filters
from plugins.funciones.graficador import Graficador

global funcion_valida
funcion_valida = True

@Client.on_message(filters.command(['graficar'], ['!','.','/']))
async def startComando(client, message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    funcion_valida = True
    
    funciones = []
    mensaje_usuario = message.text[len('/graficar') + 1:].lower()
    mensaje = await filtrarMensaje(mensaje_usuario)

    for funcion in mensaje:
        funciones.append(funcion)
    print(f'mensaje final: {mensaje}')
    print(f'funciones: {funciones}')
    graficador = Graficador()
    try:
        graficador.graficar(*funciones)
    except Exception as e:
        print(f'Error: {e}')
        await message.reply_text('Ha ocurrido un error al graficar la función.')
        return

    await message.reply_photo('output.png')

async def filtrarMensaje(mensaje):
    digitos = '0123456789'
    mensaje_corregido = ''
    try:
        for index, caracter in enumerate(mensaje):
            print(caracter)
            if caracter in digitos:
                print(f'digito: {caracter}')
            if caracter in digitos and index + 1 < len(mensaje) and mensaje[index + 1] == 'x':  # Evitar IndexErrors
                mensaje_corregido += caracter + '*'
            else:
                mensaje_corregido += caracter
        mensaje = mensaje_corregido
        if '^' in mensaje:
            mensaje = mensaje.replace('^', '**')
        if 'sqrt' in mensaje:
            mensaje = mensaje.replace('sqrt', 'np.sqrt')
        if ' ' in mensaje:
            mensaje = mensaje.replace(' ', '')
        if '&' in mensaje:
            mensaje = mensaje.split('&')
        else:
            mensaje = [mensaje]
    except Exception as e:
        funcion_valida = False
    return mensaje

