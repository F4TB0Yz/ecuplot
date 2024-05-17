from pyrogram import Client, filters
from plugins.funciones.graficador import Graficador

@Client.on_message(filters.command(['graficar'], ['!','.','/']))
async def startComando(client, message):
    user_name = message.from_user.username
    user_id = message.from_user.id

    mensaje_usuario = message.text[len('/graficar'):]
    print(mensaje_usuario)
    funciones = mensaje_usuario.split("&")
    print(f'funcion separada: {funciones}')
    funciones = [funcion.strip() for funcion in funciones]
    print(f'funciones sin espacio: {funciones}')
    funciones = [funcion.replace('^', '**') if '^' in funcion else funcion for funcion in funciones]
    print(f'funciones reemplazadas: {funciones}')
    graficador = Graficador()
    graficador.graficar(*funciones)


   

    return await message.reply_text(f"Hola **{user_name}**, bienvenido a EcundiBot.\nTu ID es **{user_id}**.")
