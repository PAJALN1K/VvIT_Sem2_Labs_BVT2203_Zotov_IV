import telebot
import time
from telebot import types
from db_work import show_day_schedule, show_week_schedule


token = "telebot_token"
bot = telebot.TeleBot(token)

week_number = int(time.strftime("%U"))
if week_number % 2 == 0:
    week_is_even = 1
else:
    week_is_even = 0

it_is_start_1 = True
it_is_start_2 = False
it_is_start_3 = False


@bot.message_handler(commands=['start'])
def start(message):
    global it_is_start_1
    it_is_start_1 = True

    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "Не хочу", "Покажи расписание")
    bot.send_message(message.chat.id,
                     'Здравствуйте! Хотите узнать свежую информацию о МТУСИ?',
                     reply_markup=keyboard)


@bot.message_handler(commands=['monday'])
def show_monday_schedule(message):
    bot.send_message(message.chat.id, show_day_schedule(0, 'Понедельник', week_is_even))


@bot.message_handler(commands=['tuesday'])
def show_tuesday_schedule(message):
    bot.send_message(message.chat.id, show_day_schedule(0, 'Вторник', week_is_even))


@bot.message_handler(commands=['sreda'])
def show_sreda_schedule(message):
    bot.send_message(message.chat.id, show_day_schedule(0, 'Среда', week_is_even))


@bot.message_handler(commands=['thursday'])
def show_thursday_schedule(message):
    bot.send_message(message.chat.id, show_day_schedule(0, 'Четверг', week_is_even))


@bot.message_handler(commands=['friday'])
def show_friday_schedule(message):
    bot.send_message(message.chat.id, show_day_schedule(0, 'Пятница', week_is_even))


@bot.message_handler(commands=['week'])
def show_this_week_schedule(message):
    bot.send_message(message.chat.id, show_week_schedule(1, week_is_even))


@bot.message_handler(commands=['nextweek'])
def show_next_week_schedule(message):
    bot.send_message(message.chat.id, show_week_schedule(0, int(not week_is_even)))


@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'Сайт МТУСИ - Лучший сайт - https://mtuci.ru/')


@bot.message_handler(commands=['help'])
def give_help(message):
    bot.send_message(message.chat.id,
                     "Я бот, который может отображать расписание группы БВТ2203 и сайт МТУСИ."
                     "\n\nСПИСОК МОИХ КОМАНД"
                     "\n /start - начало"
                     "\n /monday - отобразить расписание на понедельник"
                     "\n /tuesday - отобразить расписание на вторник"
                     "\n /sreda - отобразить расписание на среду"
                     "\n /thursday - отобразить расписание на четверг"
                     "\n /friday - отобразить расписание на пятницу"
                     "\n /week - отобразить расписание на эту неделю"
                     "\n /nextweek - отобразить расписание на следующую неделю"
                     "\n /mtuci -отобразить сайт МТУСИ"
                     )


@bot.message_handler(content_types=['text'])
def answer(message):
    global it_is_start_1, it_is_start_2, it_is_start_3

    if message.text.lower() == "хочу" and it_is_start_1:
        it_is_start_1, it_is_start_2, it_is_start_3 = False, True, False
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("А что еще ты умеешь?")
        bot.send_message(message.chat.id,
                         'Тогда Вам сюда - https://mtuci.ru/',
                         reply_markup=keyboard)
    elif message.text.lower() == "не хочу" and it_is_start_1:
        bot.send_message(message.chat.id, 'Понимаю\nХорошего Вам дня')
        exit()

    elif message.text.lower() == "а что еще ты умеешь?" and it_is_start_2:
        it_is_start_1, it_is_start_2, it_is_start_3 = False, False, True
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("Хочу", "Не хочу")
        bot.send_message(message.chat.id,
                         'Хорошо, что Вы спросили!'
                         '\nЯ умею показывать расписание группы БВТ2203.\nХотите, покажу?',
                         reply_markup=keyboard)

    elif (message.text.lower() == "хочу" and it_is_start_3)\
            or message.text.lower() == "покажи расписание":
        it_is_start_1, it_is_start_2, it_is_start_3 = False, False, False

        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row(
            "a. Понедельник",
            "b. Вторник",
            "c. Среда",
            "d. Четверг",
            "e. Пятница"
        )
        keyboard.row(
            "f. Расписание на текущую неделю",
            "g. Расписание на следующую неделю"
        )
        keyboard.row(
            "h. Помощь",
            "i. Сайт МТУСИ"
        )
        bot.send_message(message.chat.id,
                         'Выберите удовлетворяющий Вас вариант ответа.',
                         reply_markup=keyboard)
    elif message.text.lower() == "не хочу" and it_is_start_3:
        it_is_start_1, it_is_start_2, it_is_start_3 = False, False, False
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("Помощь", "Покажи расписание")
        bot.send_message(message.chat.id,
                         'Понимаю Вас. '
                         'Если Вам потребуется помощь, нажмите соответствующую кнопку '
                         'или введите команду "/help".', reply_markup=keyboard)

    elif message.text == "a. Понедельник":
        bot.send_message(message.chat.id, show_day_schedule(0, 'Понедельник', week_is_even))
    elif message.text == "b. Вторник":
        bot.send_message(message.chat.id, show_day_schedule(0, 'Вторник', week_is_even))
    elif message.text == "c. Среда":
        bot.send_message(message.chat.id, show_day_schedule(0, 'Среда', week_is_even))
    elif message.text == "d. Четверг":
        bot.send_message(message.chat.id, show_day_schedule(0, 'Четверг', week_is_even))
    elif message.text == "e. Пятница":
        bot.send_message(message.chat.id, show_day_schedule(0, 'Пятница', week_is_even))
    elif message.text == "f. Расписание на текущую неделю":
        bot.send_message(message.chat.id, show_week_schedule(1, week_is_even))
    elif message.text == "g. Расписание на следующую неделю":
        bot.send_message(message.chat.id, show_week_schedule(0, int(not week_is_even)))
    elif message.text == "h. Помощь" or message.text.lower() == "помощь":
        bot.send_message(message.chat.id,
                         "Я бот, который может отображать расписание группы БВТ2203 и сайт МТУСИ."
                         "\n\nСПИСОК МОИХ КОМАНД"
                         "\n /start - начало"
                         "\n /monday - отобразить расписание на понедельник"
                         "\n /tuesday - отобразить расписание на вторник"
                         "\n /sreda - отобразить расписание на среду"
                         "\n /thursday - отобразить расписание на четверг"
                         "\n /friday - отобразить расписание на пятницу"
                         "\n /week - отобразить расписание на эту неделю"
                         "\n /nextweek - отобразить расписание на следующую неделю"
                         "\n /mtuci -отобразить сайт МТУСИ"
                         )
    elif message.text == "i. Сайт МТУСИ":
        bot.send_message(message.chat.id,
                         "Сайт МТУСИ - Лучший сайт - https://mtuci.ru/")
    else:
        bot.send_message(message.chat.id,
                         'Извините, я Вас не понял. Проверьте правильность ввода команды.')


bot.polling(none_stop=True, interval=0)
