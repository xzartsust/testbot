from logging import ERROR, error
import telebot
from telebot import types
from telebot.apihelper import ApiHTTPException, ApiTelegramException, ApiException

bot = telebot.TeleBot('1400963433:AAGbIIlBPo0c1SwUcBaag_S_9h7KpTFhLSU')

number = []
print(number)

@bot.message_handler(commands = ['start'])
def get_contact(message):

    if message.from_user.id not in number:
        number.append(message.from_user.id)

    print(number)

@bot.message_handler(commands = ['send'])
def send(message):

    try:
        for i in range(len(number)):
            bot.send_message(number[i], 'test')
    except ApiException:
        print('no')

if __name__ == "__main__":
    bot.polling(none_stop = True, interval = 0)
