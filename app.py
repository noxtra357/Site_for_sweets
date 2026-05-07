from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# Секретный ключ, чтобы корзина не была пустой
app.secret_key = 'super_secret_key_for_sweets_shop_2026'

# Настройка базы данных SQLite
db_path = os.path.join(os.path.dirname(__file__), 'bakery.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Модель товара в магазине
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.String(255), nullable=False)


# Модель заказа клиента
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    items = db.Column(db.Text, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)


# Создание базы данных и заполнение начальными товарами, если она пуста
with app.app_context():
    db.create_all()
    if not Product.query.first():
        initial_items = [
            {"name": "Зефирный Лотос", "price": 180,
             "img": "https://www.marybakery.ru/wp-content/uploads/2017/08/zefir-14.jpg",
             "desc": "Яблочное облако с экстрактом роз."},
            {"name": "Эклер Royal", "price": 220, "img": "https://torty.ru/wp-content/uploads/2019/12/item_1214-1.jpg",
             "desc": "Бурбонская ваниль и пищевое золото."},
            {"name": "Круассан Classic", "price": 150,
             "img": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=600",
             "desc": "Натуральное сливочное масло."}
        ]
        for item in initial_items:
            db.session.add(Product(**item))
        db.session.commit()


# Главная страница
@app.route('/')
def index():
    products = Product.query.all()
    cart = session.get('cart', {})
    cart_count = sum(item['quantity'] for item in cart.values())
    return render_template('index.html', products=products, cart_count=cart_count)


# Добавление товара в корзину
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    cart = session.get('cart', {})

    p_id = str(product_id)
    if p_id in cart:
        cart[p_id]['quantity'] += 1
    else:
        cart[p_id] = {'name': product.name, 'price': product.price, 'quantity': 1}

    session['cart'] = cart
    session.modified = True
    return redirect(url_for('index'))


# Просмотр корзины
@app.route('/cart')
def show_cart():
    cart = session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total=total)


# Очистить корзину полностью
@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('show_cart'))


# Оформление заказа и запись в базу данных
@app.route('/checkout', methods=['POST'])
def checkout():
    cart = session.get('cart', {})
    if not cart:
        return redirect(url_for('index'))

    name = request.form.get('name')
    phone = request.form.get('phone')
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    items_str = ", ".join([f"{v['name']} (x{v['quantity']})" for v in cart.values()])

    new_order = Order(customer_name=name, phone=phone, items=items_str, total_price=total)
    db.session.add(new_order)
    db.session.commit()

    session.pop('cart', None)  # Чистим корзину после отправки
    return render_template('success.html', name=name, total=total)


# Добавление нового десерта через админку
@app.route('/admin/add', methods=['POST'])
def add_product():
    new_p = Product(
        name=request.form['name'],
        price=int(request.form['price']),
        img=request.form['img'],
        desc=request.form['desc']
    )
    db.session.add(new_p)
    db.session.commit()
    return redirect(url_for('index'))


# Мгновенное удаление товара
@app.route('/delete/<int:id>')
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
    return redirect(url_for('index'))


# Админка
@app.route('/admin')
def admin():
    orders = Order.query.all()
    return render_template('admin.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True)





# {"name": "Название", "price": 100, "img": "ссылка_на_фото", "desc": "Описание"},