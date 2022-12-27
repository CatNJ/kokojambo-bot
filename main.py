import config
import logging

from botdb import User
from aiogram import Bot, Dispatcher, executor, types
from art import *

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

tprint('Bot started!')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = User(message.from_user.id)
    user.check_user()

    text1 = '''
🙋‍♂ Привет! Я Tvoja mama bot.

📜 Чтобы посмотреть статистику, напиши команду "Профиль".

📘 Чтобы посмотреть перечень команд "Команды".
'''

    await message.reply(text1)


# профиль - информация о пользователе
@dp.message_handler(regexp='^Профиль')
async def prof(message: types.Message):
    user = User(message.from_user.id)
    user.check_user()

    text1 = f"""
🤚 Снова привет, Держи свою статистику.

💳 Ваш ID: {user.user_info()[0]}
🗒 Статус: {user.user_info()[1]}
💶 Баланс: {user.user_info()[2]}
📊 Ваш уровень: {user.lvl_top()}
🔩 Размер хуя: {user.user_info()[3]} см
🗒 Место работы: {user.user_info()[5]}
🧾 Имя: {user.user_info()[6]}
"""
    await message.reply(text1)


# commands
@dp.message_handler(regexp='Команды')
async def commands_list(message: types.Message):
    user = User(message.from_user.id)
    user.check_user()

    text1 =  '''
🤚 Hello guys, держите список команд.	

📜 Профиль - Посмотреть инфу о себе.
📘 Команды - Посмотреть перечень команд.
🎰 Казино - Казино <сума>.
🗒 Работы - Список работ.
👩‍🚒 Работать - Вы сходите на работу и получите оплату.
🔎 Инфа - Для просмотра информации о всём, "Инфа хелп" чтобы увидеть список.
👛 Баланс или Б - Узнать количество средств.

            '''
    await message.reply(text1)


# РАБОТЫ

# работать - получать зарплату
@dp.message_handler(regexp='Работать')
async def job_work(message: types.Message):
    user = User(message.from_user.id)
    user.check_user()

    if user.user_info()[5] == 'ферма':
        user.get_money(50000)

        first_lvl = user.lvl_top()

        await message.reply('👨‍🌾 Вы успешно собрали сено и получили 50к грн!')

        user.give_lvl(7)
        second_lvl = user.lvl_top()

        if first_lvl < second_lvl:
            await message.reply(f'🎆 Поздравляю, ваш уровень повышен до {second_lvl}')

    if user.user_info()[5] == 'Такси':
        user.get_money(90000)
        first_lvl = user.lvl_top()

        await message.reply('🚕 Вы успешно подвезли пасажиров и получили 90к грн')

        user.give_lvl(14)
        second_lvl = user.lvl_top()

        if first_lvl < second_lvl:
            await message.reply(f'🎆 Поздравляю, ваш уровень повышен до {second_lvl}')

    if user.user_info()[5] == 'Полиция':
        user.get_money(140000)
        first_lvl = user.lvl_top()

        await message.reply('👨‍🌾 Вы успешно поймали розбийныка и получили 140к грн!')

        user.give_lvl(20)
        second_lvl = user.lvl_top()

        if first_lvl < second_lvl:
            await message.reply(f'🎆 Поздравляю, ваш уровень повышен до {second_lvl}')

    if user.user_info()[5] == 'Программист':
        user.get_money(200000)
        first_lvl = user.lvl_top()

        await message.reply('👨‍🌾 Вы успешно взломали пентагон на html и получили 200к грн!')

        user.give_lvl(35)
        second_lvl = user.lvl_top()

        if first_lvl < second_lvl:
            await message.reply(f'🎆 Поздравляю, ваш уровень повышен до {second_lvl}')

    if user.user_info()[5] == 'Бодибилдер':
        user.get_money(270000)
        first_lvl = user.lvl_top()

        await message.reply('👨‍🌾 Вы выиграли соревнования и получили 270к грн!')

        user.give_lvl(50)
        second_lvl = user.lvl_top()

        if first_lvl < second_lvl:
            await message.reply(f'🎆 Поздравляю, ваш уровень повышен до {second_lvl}')

    if user.user_info()[5] == 'Врач':
        user.get_money(350000)
        first_lvl = user.lvl_top()

        await message.reply('👨‍🌾 Вы провели успешную операцию и получили 350к грн!')

        user.give_lvl(70)
        second_lvl = user.lvl_top()

        if first_lvl < second_lvl:
            await message.reply(f'🎆 Поздравляю, ваш уровень повышен до {second_lvl}')

    else:
        await message.reply('😦 Упс, похоже что-то пошло не так')


# описание и список работ
@dp.message_handler(regexp='Работы')
async def job(message: types.Message):
    user = User(message.from_user.id)
    user.check_user()

    text1 = '''
🧑‍💼 Ищешь работу? Ты попал по адресу!

👨‍🌾 Работать фермером: /job ферма - с 1 уровня
🚕 Работать таксистом: /job такси - с 5 уровня
👮‍♂ Работать полицейским: /job полиция - С 10 уровня
🧑‍💻 Работать программистом: /job программист - С 20 уровня
🏋 Работать спортсменом: /job бодибилдер - С 30 уровня
🧑‍⚕️Работать врачом: /job врач - С 45 уровня

                '''

    await message.reply(text1)


# устроиться на работу
@dp.message_handler(commands=['job'])
async def job(message: types.Message):
    user = User(message.from_user.id)
    user.check_user()

    msg_txt = message.text

    text1 = '''
🎆 Поздравляю, теперь ты работаешь на ферме!
                
🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа ферма"
        '''
    text2 = '''
🎆 Поздравляю, теперь ты работаешь в такси!
            
🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа такси" 
            '''
    text3 = '''
🎆 Поздравляю, теперь ты работаешь полицейским!

🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа полицейский" 
            '''

    text4 = '''
🎆 Поздравляю, теперь ты работаешь в гугле!

🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа программист" 
            '''

    text5 = '''
🎆 Точно! Давно нужно перестать бухать и занятся спортом.

🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа бодибилдер" 
            '''

    text6 = '''
🎆 Хороший выбор, спасать людей благое дело!

🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа врач" 
            '''

    if user.user_info()[5] == msg_txt[5:]:
        await message.reply('😯 Похоже вы уже здесь работаете')

    elif msg_txt[5:] == 'ферма':
        user.job_add(message.text[5:])
        await message.reply(text1)

    elif msg_txt[5:] == 'такси':
        lvl = user.lvl_top()
        if lvl >= 5:
            user.job_add(message.text[5:])
            await message.reply(text2)

        else:
            await message.reply('❌ Вы не можете устроиться на эту работу!')


    elif msg_txt[5:] == 'полиция':
        lvl = user.lvl_top()
        if lvl >= 10:

            user.job_add(message.text[5:])
            await message.reply(text3)

        else:
            await message.reply('❌ Вы не можете устроиться на эту работу!')


    elif msg_txt[5:] == 'программист':
        lvl = user.lvl_top()
        if lvl >= 20:
            user.job_add(message.text[5:])
            await message.reply(text4)

        else:
            await message.reply('❌ Вы не можете устроиться на эту работу!')


    elif msg_txt[5:] == 'бодибилдер':
        lvl = user.lvl_top()
        if lvl >= 30:
            user.job_add(message.text[5:])
            await message.reply(text5)

        else:
            await message.reply('❌ Вы не можете устроиться на эту работу!')


    elif msg_txt[5:] == 'Врач':
        lvl = user.lvl_top()
        if lvl >= 45:
            user.job_add(message.text[5:])
            await message.reply(text6)

        else:
            await message.reply('❌ Вы не можете устроиться на эту работу!')


    else:
        await message.reply('😦 Упс, похоже что-то пошло не так')


# операции с деньгами

# посмотреть баланс
@dp.message_handler(regexp="^(Баланс|Б)")
async def balans(message: types.Message):
    user = User(message.from_user.id)
    user.check_user()

    if message.text[:1] == 'б' or 'б':
        await message.reply(f'👛 Сума на твоём балансе равна {user.user_info()[2]}')


# ИНФО
@dp.message_handler(regexp='^Инфа')  # info
async def info(message: types.Message):
    user = User(message.from_user.id)
    user.check_user()

    text1 = '''
Вот что ты можешь у меня узнать:

Информация о роботе - Инфа работа
            '''

    text2 = '''
С помощью команды "Работы" - Вы сможете узнать перечень работ и как на них устроиться :)

Команда /job <выбраная работа> - Отвечает за зачисление на работу.

Используя команду "Работать" - Вы сходите на работу и получите оплату.
                '''

    if message.text == 'Инфа хелп':
        await message.reply(text1)

    elif message.text == 'Инфа работа':
        await message.reply(text2)

    else:
        await message.reply('😦 Упс, похоже что-то пошло не так')


# ИГРЫ

# казино


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
