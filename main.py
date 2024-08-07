import telebot
bot = telebot.TeleBot("7117174337:AAFV-qNWFY_6mFKudcT-GfPQUE2GyQ7NIiE")

@bot.message_handler(commands=["старт"])
def main1(message):
    bot.send_message(message.chat.id, "Привет, путник")

@bot.message_handler(commands=["тгк"])
def main2(message):
    bot.send_message(message.chat.id, "*держи* [тгк](https://t.me/hmhmlk)")

@bot.message_handler(commands=["мотивирующая цитатка"])
def main3(message):
    bot.send_message(message.chat.id, "Ключом к успешному лидерству сегодня является влияние, а не авторитет")

@bot.message_handler(commands=["факт об акулах"])
def main4(message):
    bot.send_message(message.chat.id, "Акулы впадают в кому, если переворачиваются вверх ногами")