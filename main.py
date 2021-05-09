from flask import Flask, url_for, request, render_template, redirect

from config import *

app = Flask(__name__)

""" Создание структуры продуктов """
# За детальной информацией перейдите в config.py

# Чтобы видеть созданную структуру: измените 0 на 1, на строчке ниже. Чтобы не видеть созданную структуру: измените 1 на 0, на строчке ниже
pr = ProductsStructure(logs = 1)

pr.create_product_structure()

""" Подготовка глобальных данных """

global_data = {
	"NAME_SHOP":NAME_SHOP,
}

""" Подключение урл путей """
@app.route('/')
def index():

	return_data = {
		"PRODUCTS": pr.products,
	}

	return render_template('index.html', data=return_data, global_data=global_data)

@app.route('/<int:id>')
def product(id):
	product = pr.search_to_structure(id)

	return render_template('product_info.html', data=product, global_data=global_data)

@app.route('/order/<int:id>', methods=["GET", "POST"])
def order(id):

	if request.method == 'POST':

		product = pr.search_to_structure(id)

		with open('orders.txt', 'a', encoding='utf-8') as file:
		    file.write(
		    	f"[{GetTime()}] Заказ оформлен. Номер телефона: {request.form['phone_number']}. "
		    	f"Информация о заказе: Название {product['name']} | Краткое описание: {product['short_description']} | Цена: {product['price']}\n")

		return redirect(url_for('index'))

	return redirect(url_for('product', id=id))


if __name__ == "__main__":

	# Чтобы убрать режим дебага измените параметр True на False
	app.run(debug=True)