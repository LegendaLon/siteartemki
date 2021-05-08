from datetime import datetime as dt

NAME_SHOP = "Магазин"

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

		self.log_status = logs

	def logs(self):
		print("===========[START PRINT LOG]===========")
		for a in self.products:
			print("===[ID:" + str(a["id"]) + "]===")
			print("NAME: " + a["name"])
			print("DESCRIPTION: " + a["description"])
			if a["description"] != a["short_description"]:
				print("SHORT_DESCRIPTION: " + a ["short_description"])
			print("PRICE: " + a["price"])
			print("===[END]===")
			print("\n")

		print("===========[END PRINT LOG]===========")

	def add_product(self, name=None, description=None, price=None):

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