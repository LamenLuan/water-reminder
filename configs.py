from watertime import WaterTime

APP_NAME = "Water reminder"
CONFIG_FILE_PATH = "data"
DEFAULT_AMOUNT_TO_DRINK = 2000
DEFAULT_SIP_AMOUNT = 250

DEFAULT_START_TIME_1 = WaterTime("7:30")
DEFAULT_LUNCH_TIME = WaterTime("12:00")
DEFAULT_START_TIME_2 = WaterTime("13:15")
DEFAULT_END_TIME = WaterTime("17:30")

TIMES = [DEFAULT_START_TIME_1, DEFAULT_LUNCH_TIME, DEFAULT_START_TIME_2, DEFAULT_END_TIME]

def write_default_data_in_file():
	with open(CONFIG_FILE_PATH, "w") as file:
		file.write(f"{DEFAULT_AMOUNT_TO_DRINK}\n{DEFAULT_SIP_AMOUNT}\n")
		t = [DEFAULT_START_TIME_1, DEFAULT_LUNCH_TIME, DEFAULT_START_TIME_2, DEFAULT_END_TIME]
		values = [str(time) for time in t]
		file.write("\n".join(values))