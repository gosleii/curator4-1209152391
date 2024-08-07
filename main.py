import telebot
bot = telebot.TeleBot("7117174337:AAFV-qNWFY_6mFKudcT-GfPQUE2GyQ7NIiE")

@bot.message_handler(commands=["start"])
def main1(message):
    bot.send_message(message.chat.id, "Привет, путник")

@bot.message_handler(commands=["command1"])
def main2(message):
    bot.send_message(message.chat.id, "*держи [тгк](https://t.me/hmhmlk)*", parse_mode="Markdown")

@bot.message_handler(commands=["command2"])
def main3(message):
    bot.send_message(message.chat.id, "Ключом к успешному лидерству сегодня является влияние, а не авторитет")

@bot.message_handler(commands=["command3"])
def main4(message):
    bot.send_message(message.chat.id, "Акулы впадают в кому, если переворачиваются вверх ногами")

bot.infinity_polling()