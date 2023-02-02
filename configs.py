CONFIG_FILE_PATH = "data"
DEFAULT_AMOUNT_TO_DRINK = 2000
DEFAULT_SIP_AMOUNT = 250

def write_default_data_in_file():
	with open(CONFIG_FILE_PATH, "w") as file:
		file.write(f"{DEFAULT_AMOUNT_TO_DRINK}\n{DEFAULT_SIP_AMOUNT}")