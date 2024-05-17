from pyrogram import Client, filters

@Client.on_message(filters.command(['start'], ['!','.','/']))
async def startComando(client, message):
    user_name = message.from_user.username
    user_id = message.from_user.id

    return await message.reply_text(f"Hola **{user_name}**, bienvenido a Ecuplot.\nTu ID es **{user_id}**.", reply_to_message_id=message.id)