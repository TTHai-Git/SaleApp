import math, untils

from flask import render_template, request, url_for, session, jsonify
from flask_login import login_user

from app import dao, app, login
from app.admin import *


@app.route("/")
def trangchu():
    kw = request.args.get("kw")
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')
    #categories = dao.loadcategories()
    count_products = dao.count_products()
    products = dao.loadproducts(kw, cate_id, page)

    return render_template('index.html', products=products,
                           pages=math.ceil(count_products / app.config['PAGE_SIZE']))


@app.route('/register', methods=['get', 'post'])
def user_register():
    err_msg = ""
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        repeatpassword = request.form.get('repeatpassword')
        email = request.form.get('email')
        try:
            if password.strip().__eq__(repeatpassword.strip()):
                dao.add_user(name=name, username=username, password=password, email=email)
                return redirect(url_for('user_login'))
            else:
                err_msg = 'Mat Khau KHONG Khop!!!'

        except Exception as ex:
            err_msg = 'He thong dang co loi !!!' + str(ex)
    return render_template('register.html', err_msg=err_msg)


@app.context_processor
def common_response():
    return {
        'categories': dao.loadcategories(),
        'cart': untils.count_cart(session.get('cart'))
    }


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route("/admin-login", methods=['POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = dao.get_user(username, password)
        if user:
            login_user(user=user, remember=False)
    return redirect("/admin")


@app.route("/login", methods=['POST', 'GET'])
def user_login():
    err_msg = ""
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = dao.get_user(username, password)
        try:
            if user:
                return redirect(url_for('trangchu'))
            else:
                err_msg = 'ĐĂNG NHẬP THẤT BẠI VUI LÒNG KIỂM TRA LẠI UserName Hoặc PassWord!!!'
        except Exception as ex:
            err_msg = "ĐĂNG NHẬP THẤT BẠI NGƯỜI DÙNG %s KHÔNG TỒN " % username
    return render_template('login.html', err_msg=err_msg)


@app.route('/api/cart', methods=['post'])
def add_to_cart():
    """
    {
        "cart":{
            "1":{
                "id": "1",
                "name": "ABC",
                "price": 12,
                "quantity": 2
            }, "2": {
                "id": "2",
                "name": "ABC",
                "price": 12,
                "quantity": 1
            }
        }
    }
    :return:
    """
    data = request.json

    cart = session.get('cart')
    if cart is None:
        cart = {}
    id = str(data.get('id'))
    if id in cart:  # sản phẩm đã có trong giỏ chưa
        cart[id]['quantity'] += 1  # tăng sl sản phẩm lên 1
    else:  # sản phẩm chưa có trong giỏ
        cart[id] = {
            "id": id,
            "name": data.get('name'),
            "price": data.get('price'),
            "quantity": 1
        }
    session['cart'] = cart
    print(cart)

    # return jsonify({
    #     "total_amount": 100,
    #     "total_quantity": 10,
    # })

    return untils.count_cart(cart)

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == "__main__":
    app.run(debug=True)
