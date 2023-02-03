import datetime

class WaterTime:
	def __init__(self, date_time_str: str) -> None:
		self.horas, self.minutos = map(int, date_time_str.split(":"))

	def __str__(self) -> str:
		return f"{self.horas:02d}:{self.minutos:02d}"

	def to_datetime(self):
		data = datetime.now()
		return data.replace(hour=self.horas, minute=self.minutos, second=0, microsecond=0)