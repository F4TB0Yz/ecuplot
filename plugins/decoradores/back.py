from pyrogram.types import InlineKeyboardButton

class DecoradoresBackButton:
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

        self.back_mensaje = f"""
𝙀𝙘𝙪𝙥𝙡𝙤𝙩                © 2024

Menu Principal
"""