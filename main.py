import telebot
from telebot import types

bot = telebot.TeleBot ('6584648573:AAFGWYO4-NXUUI4GJLnCUk1wyX5jyVsey94')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать персонажа")
    btn2 = types.KeyboardButton("Почитать лор")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Привет путник! Здесь должно быть приветственное слово, но мы его еще не придумали", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Выбрать персонажа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('ТАУРАН')
        btn2 = types.KeyboardButton('ГНОМБАФЫ')
        btn3 = types.KeyboardButton('АНГЕЛ')

        markup.add(btn1, btn2,btn3)
        bot.send_message(message.from_user.id, 'Выбери одного из персонажей.', reply_markup=markup) #ответ бота

    elif message.text == 'Почитать лор':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Выбор персонажа')
        btn2 = types.KeyboardButton('исчЁ')

        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'История этого мира древна как ... мамонта. Перейдем к выбору персонажа?', reply_markup=markup)

    elif message.text == 'исчЁ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Выбор персонажа')

        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Рано тебе еще знать всю историю. Выбирай персонажа и погнали')
    elif message.text == 'ТАУРАН':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Выбираю тебя')


        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Дитя нежной любви человека к природе.однажды в студенцю зимнюю пору пастух решил согреть корову.Но кто же знал что они были на полянке образованной слабым источником магии жизни.Теленок получился чуть умнее мамы а ликом весь в отца.Расса тауран обладает огромной физической мощю которая позволяет им правой рукой держать Гнолла и бить им другого Гнолла а левой рукой пить молоко из кувшина.Магии нет, интелекта нет зато есть дубина.', reply_markup=markup)

    elif message.text == 'ГНОМБАФЫ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Выбираю тебя')


        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Дети гномов за дар к магии были изгнанны из подземных городов ибо нефиг выделятся.В силу запахов витающих на уровне носа получилось первое площадное заклинание очистки воздуха а дальше оно как поперло... Первая гильдия гномов магов и ее лидер Борг Чистый Воздух представляют вам своих адептов во временное пользование. Массовые бафы на все случаи жизни ДОРОГО.', reply_markup=markup)

    elif message.text == 'АНГЕЛ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Выбираю тебя')


        markup.add(btn1)
        bot.send_message(message.from_user.id, 'В маленькой глухой деревне однажды началась сухая гроза со странными раскатами грома. Дело то в целом обычное по весне, но тут начался странный белый дождь.Утро. Деревня скрытая в белой воде.Громовым раскатом по деревне пронесся женский крик.Все девушки деревни обнаружили что они беременны. Через 9 месяцев деревня принимала роды. Дети росли прекрасными но слишком патетичными так еще и в период созревания отращивали крылья и непреодолимую тягу нести людям добро и причинять справедливость.', reply_markup=markup)

    if message.text == 'Выбираю тебя':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
    btn5 = types.KeyboardButton('Перейти в город')
    

    markup.add(btn5)
    bot.send_message(message.from_user.id, 'Поздравляю, Выбор сделан!', reply_markup=markup)  # ответ бота

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть