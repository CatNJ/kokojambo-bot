from random import *
import config
from botdb import User
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

print('Bot started!')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):

	user = User(message.chat.id)
	user.check_user(message.chat.id)

	await message.reply('''
🙋‍♂ Привет! Я Milan bot.

📜 Чтобы посмотреть статистику, напиши команду "Профиль".

📘 Чтобы посмотреть перечень команд "Команды".
''')


@dp.message_handler(regexp='Профиль')
async def prof(message: types.Message):

	user = User(message.chat.id)
	user.check_user(message.chat.id)


	await message.reply(
		f"""
		🤚 Снова привет, Держи свою статистику.
		
		💳 Ваш ID: {user.user_info(message.from_user.id)[0]}
		🗒 Статус: {user.user_info(message.from_user.id)[1]}
		💶 Баланс: {user.user_info(message.from_user.id)[2]}
		📊 Ваш уровень: {user.lvl_top()}
		🔩 Размер хуя: {user.user_info(message.from_user.id)[3]} см
		🗒 Место работы: {user.user_info(message.from_user.id)[5]}
		
		""")


@dp.message_handler(regexp='Команды')
async def commands_list(message: types.Message):

	user = User(message.chat.id)
	user.check_user(message.chat.id)

	await message.reply(
		'''
		🤚 Hello guys, держите список команд.	
			
		📜 Профиль - Посмотреть инфу о себе.
		📘 Команды - Посмотреть перечень команд.
		🎰 Казино - Казино {сума}.
		🗒 Работа - Работать, вся инфа будет в сообщении.		
		🔎 Инфа - Для просмотра информации о всём, "Инфа хелп" чтобы увидеть список.
		
		''')


@dp.message_handler(regexp='Работать')
async def job_work(message: types.Message):
	user = User(message.chat.id)
	user.check_user(message.chat.id)






@dp.message_handler(regexp='Работа')
async def job(message: types.Message):

	user = User(message.chat.id)
	user.check_user(message.chat.id)

	await message.reply(
		'''
		🧑‍💼 Ищешь работу? Ты попал по адресу!
		
		👨‍🌾 Работать фермером: /job ферма - с 1 уровня
		
		🚕 Работать таксистом: /job такси - с 3 уровня
		
		👮‍♂ Работать полицейским: /job полиция - С 5 уровня
		
		🧑‍💻 Работать программистом: /job программист - С 6 уровня
		
		🏋 Работать спортсменом: /job бодибилдер - С 7 уровня
		
		🧑‍⚕️Работать врачом: /job врач - С 8 уровня
		
		
		
		''')



@dp.message_handler(commands=['job'])
async def job(message: types.Message):
	user = User(message.chat.id)
	user.check_user(message.chat.id)


	if user.user_info(message.from_user.id)[5] == message.text[5:]:
		await message.reply('😯 Похоже вы уже здесь работаете')


	elif message.text[5:] == 'ферма':
		user.job_add(message.text[5:])
		await message.reply('''
		🎆 Поздравляю, теперь ты работаешь на ферме!
				
		🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа ферма"
		''')

	elif message.text[5:] == 'такси':
		lvl = user.lvl_top()
		if lvl >= 3:
			user.job_add(message.text[5:])
			await message.reply('''
			🎆 Поздравляю, теперь ты работаешь в такси!
			
			🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа такси" 
			''')

		else:
			await message.reply('❌ Вы не можете устроиться на эту работу!')


	elif message.text[5:] == 'полиция':
		lvl = user.lvl_top()
		if lvl >= 5:
			user.job_add(message.text[5:])
			await message.reply('''
			🎆 Поздравляю, теперь ты работаешь полицейским!

			🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа полицейский" 
			''')

		else:
			await message.reply('❌ Вы не можете устроиться на эту работу!')


	elif message.text[5:] == 'программист':
		lvl = user.lvl_top()
		if lvl >= 6:
			user.job_add(message.text[5:])
			await message.reply('''
			🎆 Поздравляю, теперь ты работаешь в гугле!

			🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа программист" 
			''')

		else:
			await message.reply('❌ Вы не можете устроиться на эту работу!')


	elif message.text[5:] == 'бодибилдер':
		lvl = user.lvl_top()
		if lvl >= 7:
			user.job_add(message.text[5:])
			await message.reply('''
			🎆 Точно! Давно нужно перестать бухать и занятся спортом.

			🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа бодибилдер" 
			''')

		else:
			await message.reply('❌ Вы не можете устроиться на эту работу!')


	elif message.text[5:] == 'Врач':
		lvl = user.lvl_top()
		if lvl >= 8:
			user.job_add(message.text[5:])
			await message.reply('''
			🎆 Хороший выбор, спасать людей благое дело!

			🔎 Чтобы посмотреть информацию о своей роботе напишите "Инфа врач" 
			''')

		else:
			await message.reply('❌ Вы не можете устроиться на эту работу!')


	else:
		await message.reply('😦 Упс, похоже что-то пошло не так')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
