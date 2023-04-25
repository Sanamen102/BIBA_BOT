import telebot

with open('token.txt', 'r') as f:
    token = f.read().strip()
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Любое сообщение шифруется")

@bot.message_handler(func=lambda message: True)
def send_crypted_message(message):
    alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    smeshenie  = 3 # Ключ шифрования
    itog  = ''
    mess=message.text;
    mess=mess.upper()
    for i in mess:
            mesto = alfavit.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit:
                itog += alfavit[new_mesto]  # Задаем значения в итог
            else:
                itog += i
    bot.reply_to(message, f"{itog}")

bot.polling()