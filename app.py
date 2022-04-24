import re
import telebot
from config import TOKEN, keys
from utils import MassCalculation, CalculationException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите боту формулу вещества. \n \
Вводите вещество латинскими буквами. Если индекс после элемента - 1, его надо написать.'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def result(message: telebot.types.Message):
    try:
        vvod = message.text
        substance = re.sub('(?<=\d)(?!\d)|(?<!\d)(?=\d)', ' ', vvod)
        list_elements = substance.split()
        elements = ' '.join(list_elements)

        list_numbers = []
        num = ''
        for char in elements:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                    list_numbers.append(int(num))
                    num = ''
        if num != '':
            list_numbers.append(int(num))

        string_numbers = [str(item) for item in list_numbers]

        list_letters = list_elements + string_numbers
        string_elements = []
        for i in list_letters:
            if i not in string_elements:
                string_elements.append(i)
            else:
                string_elements.remove(i)

        leng = len(string_elements)
        num = 0
        mass = 0
        while num < leng:
            mass = mass + float(keys[string_elements[num]]) * float(list_numbers[num])
            num += 1


    except CalculationException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду. \n{e}')

    else:
        text = 'Молекулярная масса вещества равна', mass, 'г/моль'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
