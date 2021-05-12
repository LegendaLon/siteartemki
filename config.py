from datetime import datetime as dt
from prettytable import PrettyTable

from colorama import Fore

NAME_SHOP = "Магазин"

SETTING_TEMPLATE = {
	"index":"index.html",
	"product_info":"product_info.html",
}

""" Время """
def GetTime():
	time = str(dt.now())[11:19]
	day = str(dt.now())[8:10]
	month = str(dt.now())[5:7]
	year = str(dt.now())[0:4]

	return f"{time} {day}/{month}/{year}"

""" Структура товаров """
class ProductsStructure():
	def __init__(self, logs):
		self.products = []
		self.last_id = 1

		# Красивая таблица структуры
		self.table = PrettyTable([f"{Fore.YELLOW}ID{Fore.RESET}", f"{Fore.YELLOW}NAME{Fore.RESET}", f"{Fore.YELLOW}SHORT_DESCRIPTION{Fore.RESET}", f"{Fore.YELLOW}PRICE{Fore.RESET}"])

		# Вывод итоговой структуры в консоль
		self.log_status = logs

	def logs(self):
		# Добавление товаров в таблицу, для красиового вывода
		for product in self.products:
			self.table.add_row([product['id'], product["name"], product["short_description"], product["price"]])

		print(self.table)

	def add_product(self, name=None, description=None, price=None):
		# Добавление товаров
		product = {
			"id":self.last_id,
			"name":name,
			"price":price,
			"description":description,
		}
		if len(description) >= 60: 
			product["short_description"] = description[:60] + "..."
		else:
			product["short_description"] = description

		self.last_id += 1

		self.products.append(product)

	def search_to_structure(self, id):
		# Поиск по структуре
		for product in self.products:
			if product['id'] == id:
				return product

	""" Ниже прописываем создание всех продуктов в сттруктуре """
	def create_product_structure(self):
		# Пример
		# self.add_product(name="Название продукта", description="Описание продукта", price="Стоимость продукта")
		# Можно просто копировать и просто изменять параметры

		self.add_product(name="Картошка", description="Отборная Беларусская", price="200$")
		self.add_product(name="Сало", description="Отборное Украинское", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Пиво", description="Отборный Чешское", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")
		self.add_product(name="Багет", description="Отборный Итальяский", price="200$")

		if self.log_status == 1:
			self.logs()