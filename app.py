

import telebot
# import json
# from config import *
from extensions import *
import lxml.html
# import requests

bot = telebot.TeleBot(TOKEN)
bot_name = bot.get_me().__getattribute__('username') # take the Bot name

''' Admin functions'''
# Обрабатываются все сообщения, содержащие команды '/download'. - update currency list
@bot.message_handler(commands=['downloadCurrency'])
def download(message: telebot.types.Message):
	if message.chat.username == admin:
		text = f"Currencies list has been downloaded from the site"
		line = ''
		with open('currency_list.txt', 'w') as file:
			detailed_list = {}
			list_ = json.loads(list)
			for data in list_:
				for currency, info in list_[data].items():
					detailed_list[currency] = info
				for ticker, info in detailed_list.items():
					line += f"{str(ticker)}: {str(info)}\n"
			file.write(f"{current_date}, {current_time.hour:02d}:{current_time.minute:02d}:{current_time.second:02d}\n")
			file.write(line)
	else:
		text = 'Admin access needed!'
	bot.reply_to(message, text)

# Обрабатываются все сообщения, содержащие команды '/download'. - update crypto currency list
@bot.message_handler(commands=['downloadCrypto'])
def download(message: telebot.types.Message):
	if message.chat.username == admin:
		text = f"CryptoCurrencies list has been downloaded from the site"
		tree = lxml.html.document_fromstring(crypto_url)
		line = ''
		with open('crypro_currency_list.txt', 'w') as file:
			Crypto_dict = {}
			for n, i in enumerate(range(1, 300)):
				tbody = tree.xpath(f'//*[@id="gecko-table-all"]/tbody/tr[{i}]/td[2]/div/div[2]/a/span[1]/text()')
				tbody1 = tree.xpath(f'//*[@id="gecko-table-all"]/tbody/tr[{i}]/td[3]/span/text()')
				Crypto_dict[tbody1[0]] = tbody[0]
			for ticker, info in Crypto_dict.items():
				line += f"{str(ticker)}: {str(info)}\n"
			file.write(f"{current_date}, {current_time.hour:02d}:{current_time.minute:02d}:{current_time.second:02d}\n")
			file.write(line)
	else:
		text = 'Admin access needed!'
	bot.reply_to(message, text)

# to show memory
@bot.message_handler(commands=['show'])
def memory(message: telebot.types.Message):
	if message.chat.username == admin:
		converted_cash = json.loads(red.get('cash'))
		text = f"Memory statistic, sir!:\n\n" \
               f"'help' requests: {converted_cash['help']}\n" \
               f"'currency' requests: {converted_cash['currency']}\n" \
               f"'crypto' requests: {converted_cash['crypto']}\n" \
			   f"'fullCurrecncy' requests: {converted_cash['fullCurrecncy']}\n" \
			   f"'fullCrypto' requests: {converted_cash['fullCrypto']}\n" \
			   f"'rus' requests: {converted_cash['rus']}\n" \
			   f"'convert' requests: {converted_cash['convert']}\n" \
			   f"'error' requests: {converted_cash['error']}\n\n" \
			   f"'Total' requests: {converted_cash['help']+converted_cash['currency']+converted_cash['crypto']+converted_cash['fullCurrecncy']+converted_cash['fullCrypto']+converted_cash['convert']+converted_cash['error']+converted_cash['rus']}"
	else:
		text = "Admin access needed!"
	bot.send_message(message.chat.id, text)

#to erase memory
@bot.message_handler(commands=['erase'])
def eraser(message: telebot.types.Message):
	if message.chat.username == admin:
		for key in cash.keys():
			cash[key] = 0
			red.set('cash', json.dumps(cash))
		text = "Cash has been cleaned, sir!"
	else:
		text = "Admin access needed!"
	bot.send_message(message.chat.id, text)

''' Bot '''

# # Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
	if message.chat.username == admin:
		cond = f"Welcome, sir {message.chat.first_name}!"
		admin_function = (f"\n\nAdmin functionality:\n"
			f"- Update currency list from the site: /downloadCurrency\n"
			f"- Update crypto list from the site: /downloadCrypto\n"
			f"- Show statistics: /show\n"
			f"- Clean statistics: /erase\n"
		)
	else:
		cond = f"Welcome, @{message.chat.username}"  # , {message.chat.first_name}")
		admin_function = ''
	text = (f"{cond}\n"
			f"@{bot_name} is used to get the currency exchange rate!\n\n"
	f"- To activate the @{bot_name} put your command in the following way:\n<currency ticker>\
	<converted currency ticker>\
	<amount>\nExample: USD EUR 1\n\nUseful information:\n"   #### rev 3.0
			f"- Currencies list (base): /currency\n"
			f"- Crypto list (base): /crypto\n"
			f"- Download full currencies list: /fullCurrecncy\n"
			f"- Download full crypto currencies list: /fullCrypto\n"
			f"- Change the language (Russian): /rus"
			f"{admin_function}"
			f"\nCreated by @Victor\n"
			# f"To say thanks: /thanks"
    )
	Counter.count('help')
	bot.reply_to(message, text)

# Обрабатываются все сообщения, содержащие команды '/rus'. #### rev 3.0
@bot.message_handler(commands=['rus'])
def rus(message: telebot.types.Message):
	cond = f"Добро пожаловать, @{message.chat.username}"  # , {message.chat.first_name}")
	text = (f"{cond}\n"
			f"@{bot_name} необходим для получения биржевых курсов валют!\n\n"
	f"- Чтобы активировать бота @{bot_name} введите команду следующим образом:\n<тикер валюты>\
	<тикер конвертированной валюты\
	<сумма>\nПример: USD EUR 1\n\nПолезная информация:\n"   
			f"- Список валют: /currency\n"
			f"- Список криптовалют: /crypto\n"
			f"- Скачать полный список валют: /fullCurrecncy\n"
			f"- Скачать полный список криптовалют: /fullCrypto\n"


			f"\nСоздано: @{message.chat.username}\n"
			# f"To say thanks: /thanks"
    )
	Counter.count('rus')
	bot.reply_to(message, text)


# Обрабатываются все сообщения, содержащие команды '/currency'.
@bot.message_handler(commands=['currency'])
def currency(message: telebot.types.Message):
	text = f"Currency list:"
	for i, name in enumerate(currency_list.items()): #CurrencyInfo.get_currency_list().items():
		if i <= 50:
			info_ = f"{name[0]}:{' '} {name[1]}"
			text = '\n'.join((text, info_, ))
	Counter.count('currency')
	bot.reply_to(message, text)
	text = f"Download full currencies list: /fullCurrecncy"
	bot.send_message(message.chat.id, text)


# Обрабатываются все сообщения, содержащие команды '/crypto currency'.
@bot.message_handler(commands=['crypto'])
def currency(message: telebot.types.Message):
	text = f"Crypto currency list:"
	for i, name in enumerate(crypto_currency_list.items()): #CurrencyInfo.get_currency_list().items():
		if i <= 50:
			info_ = f"{name[0]}:{' '} {name[1]}"
			text = '\n'.join((text, info_, ))
	Counter.count('crypto')
	bot.reply_to(message, text)
	text = f"Download full crypto list: /fullCrypto"
	bot.send_message(message.chat.id, text)

# Обрабатываются все сообщения, содержащие команды '/fullCrypto'.
@bot.message_handler(commands=['fullCrypto'])
def send_welcome(message):
	with open('crypro_currency_list.txt', 'rb') as file:
		# f = file.read()
		Counter.count('fullCrypto')
		bot.send_message(message.chat.id, '"crypro_currency_list.txt" has been sent')
		bot.send_document(message.chat.id, file)
	# bot.send_document(message.chat.id, document = open('crypro_currency_list.txt', 'rb'))

# Обрабатываются все сообщения, содержащие команды '/fullCurrecncy'.
@bot.message_handler(commands=['fullCurrecncy'])
def send_welcome(message):
	with open('currency_list.txt', 'rb') as file:
		# f = file.read()
		Counter.count('fullCurrecncy')
		bot.send_message(message.chat.id, '"currency_list.txt" has been sent')
		bot.send_document(message.chat.id, file)

###### rev 3.0
# Обрабатываются все сообщения, содержащие команды '/set'. - set of 3 currencies
@bot.message_handler(commands=['set'])
def set(message):
	currency = ['USD', 'EUR', 'RSD']
	base = "RUB"
	amount = '1'
	for quote in currency:
		total_base = Converter.converter(quote, base, amount)
		Counter.count('convert')
		text = f"{amount} {quote} ({currency_list[quote]}) = {total_base[base] * float(amount):2.2f} {base}"
		bot.send_message(message.chat.id, text)


# Обрабатываются все сообщения, содержащие text.
@bot.message_handler(content_types = ['text', ])
def convert(message: telebot.types.Message):
	try:
		value = message.text.split(' ')

		error_text = (f"Put your command in the following way:\n<currency ticker>\
			<converted currency ticker>\
			<amount>")

		if len(value) != 3:
			raise ConvetionExcepton(f'Command failed!\n {error_text}')

		quote, base, amount = value
		quote = quote.upper() # opportunity to use not a capital letter
		base = base.upper() # opportunity to use not a capital letter

		total_base = Converter.converter(quote, base, amount)

	except ConvetionExcepton as e:
		Counter.count('error')
		bot.reply_to(message, f"User error!\n{e}")
	except Exception as e:
		Counter.count('error')
		bot.reply_to(message, f"System error!\n{e}")
	else:
		Counter.count('convert')
		text = f"{amount} {quote} ({currency_list[quote]}) = {total_base[base] * float(amount):2.2f} {base}"
		bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
# bot.polling()