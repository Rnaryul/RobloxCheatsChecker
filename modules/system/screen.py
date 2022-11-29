################################################################################
#                              RIGHT DECISION                                  #
#                     Telegram https://t.me/+fN7NR-nVvmsxYWRi                  #
#      Если сливаете мой скрипт в свой канал. Хотя бы отметьте мой канал       #
################################################################################
from PIL import ImageGrab

def Screenshot():
	try:
		screen = ImageGrab.grab()
		screen.save(r'C:\hesoyam8927163\sreenshot.jpg')
	except Exception as e:
		print(e)