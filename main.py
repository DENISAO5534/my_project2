import pyowm
import telebot
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm =pyowm.OWM('9f395d1507f467005fcc3fcb08d6e744',config_dict)
bot = telebot.TeleBot("5681920429:AAEVvj8IAij8Uj_B3qhr3yLmoyu0oxEvJCg",parse_mode=None)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	# print(w.wind()['speed'], w.temperature('celsius')['temp'])
	weather_info = "В городе" + message.text + "сейчас" + w.detailed_status + "\n"
	weather_info += "Температура:" + str(w.temperature()('celsius')['temp']) + "\n"
	weather_info += "Скорость ветра:" + str(w.wind()['speed']) + " m/c" + "\n"

	bot.reply_to(message, weather_info)

bot.infinity_polling()









