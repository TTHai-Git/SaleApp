import math
from flask import render_template, request, session, jsonify
from flask_login import login_user, login_required

from app import login, untils
from app.admin import *


@app.route("/")
def trangchu():
    kw = request.args.get("kw")
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')
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
        avatar = request.files.get('avatar')
        try:
            if password.strip().__eq__(repeatpassword.strip()):
                dao.add_user(name=name, username=username, password=password, email=email, avatar=avatar)
                return redirect('/login')
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


@app.route("/login", methods=['POST', 'GET'])
def login():
    err_msg = ""
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = dao.get_user(username, password)
        try:
            if user:
                login_user(user=user)
                if current_user.user_role == UserRole.ADMIN:
                    return redirect('/admin')
                else:
                    Next = request.args.get('next')
                    return redirect('/' if Next is None else Next)
            else:
                err_msg = 'ĐĂNG NHẬP THẤT BẠI VUI LÒNG KIỂM TRA LẠI UserName Hoặc PassWord!!!'
        except Exception as ex:
            err_msg = "ĐĂNG NHẬP THẤT BẠI NGƯỜI DÙNG %s KHÔNG TỒN " % username
    return render_template('login.html', err_msg=err_msg)


@app.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return redirect('/login')


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


@app.route('/api/cart/<product_id>', methods=['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)
    session['cart'] = cart
    return jsonify(untils.count_cart(cart))


@app.route('/api/cart/<product_id>', methods=['delete'])
def delete_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        del cart[product_id]

    session['cart'] = cart

    return jsonify(untils.count_cart(cart))


@app.route('/api/pay', methods=['post'])
@login_required
def pay():
    try:
        dao.add_receipt(session.get('cart'))
    except:

        return jsonify({'status': 500, "err_msg": "..."})
    else:
        del session['cart']
        return jsonify({'status': 200})


@app.route('/cart', methods=['post'])
def clear_cart():
    session.pop('cart')
    return redirect('/cart')


@app.route('/cart')
def cart():
    return render_template('cart.html')


if __name__ == "__main__":
    app.run(debug=True)
