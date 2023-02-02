import ctypes
from datetime import datetime
import datetime as dt
from os.path import exists
from time import sleep
from winotify import Notification, audio

CONFIG_FILE_PATH = "data"
DEFAULT_AMOUNT_TO_DRINK = 2000
DEFAULT_SIP_AMOUNT = 250
APP_NAME = "Water reminder"

def show_toast(title: str, msg: str, duration: str):
	toast = Notification(
		app_id=APP_NAME,
		title=title,
		msg=msg,
		duration=duration,
	)
	
	toast.set_audio(audio.Reminder, loop=False)
	toast.show()

def show_quick_toast(title: str, msg: str):
	show_toast(title, msg, 'short')

def show_long_toast(title: str, msg: str):
	show_toast(title, msg, 'long')

def write_default_data_in_file():
	with open(CONFIG_FILE_PATH, "w") as file:
		file.write(f"{DEFAULT_AMOUNT_TO_DRINK}\n{DEFAULT_SIP_AMOUNT}")

def toast_data_file_error():
	show_quick_toast(
		"Erro na leitura de dados",
		"O arquivo de dados está corrompido. O arquivo será reescrito com os valores padrão",
	)

def toast_service_started():
	show_quick_toast("Servico Iniciado", "")

def toast_drink_water(sip_amount: int):
	show_long_toast("Beba água", f"Beba {sip_amount} ml de água")

def minimizeWindow():
	ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def main():
	minimizeWindow()

	if not exists(CONFIG_FILE_PATH):
		write_default_data_in_file()

	try:
		with open(CONFIG_FILE_PATH, "r") as file:
			amount_to_drink = int(file.readline())
			sip_amount = int(file.readline())
		toast_service_started()
	except ValueError:
		amount_to_drink = DEFAULT_AMOUNT_TO_DRINK
		sip_amount = DEFAULT_SIP_AMOUNT
		toast_data_file_error()
		write_default_data_in_file()

	amount_of_sips = int(amount_to_drink / sip_amount)

	start_time_1 = datetime.now().replace(hour=7, minute=30, second=0, microsecond=0)
	lunch_time = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
	start_time_2 = datetime.now().replace(hour=13, minute=15, second=0, microsecond=0)
	end_time = datetime.now().replace(hour=17, minute=30, second=0, microsecond=0)

	total_seconds = (lunch_time - start_time_1 + end_time - start_time_2).total_seconds()

	interval = int(total_seconds / amount_of_sips)

	time_to_drink = start_time_1
	pause_time = lunch_time

	times_to_drink: 'list[datetime]' = []

	for _ in range(amount_of_sips):
		time_to_drink = time_to_drink + dt.timedelta(seconds=interval)
		if time_to_drink <= pause_time:
			times_to_drink.append(time_to_drink)
		elif pause_time != end_time:
			pause_time = end_time
			time_to_drink = start_time_2
			times_to_drink.append(time_to_drink)
		else: break

	while times_to_drink:
		next_time = times_to_drink[0]
		now = datetime.now()
		
		if now < next_time:
			time_left = (next_time - now).total_seconds()
			sleep(time_left)
		else:
			while now >= next_time:
				times_to_drink.pop(0)
				if not times_to_drink: return
				next_time = times_to_drink[0]
			if now < next_time: continue

		toast_drink_water(sip_amount)
		times_to_drink.pop(0)
	
if __name__ == '__main__':
	main()