from pyrogram.types import InlineKeyboardButton

class DecoradoresAcerca:
    def __init__(self):
        self.botones = [
                [
                    InlineKeyboardButton(text='Instrucciones', callback_data='instrucciones'),
                    InlineKeyboardButton(text='Perfil', callback_data='perfil')
                ],
                [
                    InlineKeyboardButton(text='Atras', callback_data='back')
                ]
        ]

        self.acerca_mensaje = f"""
𝙀𝙘𝙪𝙥𝙡𝙤𝙩                © 2024

ʙʏ:
𝗙𝗲𝗹𝗶𝗽𝗲 𝗗𝘂𝗮𝗿𝘁𝗲
𝗝𝘂𝗹𝗶𝗮𝗻 𝗖𝗮𝗿𝗱𝗲𝗻𝗮𝘀
𝗦𝗮𝗻𝘁𝗶𝗮𝗴𝗼 𝗖𝘂𝗲𝘃𝗮𝘀
𝗘𝗱𝘂𝗮𝗿 𝗕𝗲𝗿𝗻𝗮𝗹
"""