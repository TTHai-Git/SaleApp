from flask import render_template, request, jsonify, url_for, redirect
from app import dao, app
from app.admin import *


@app.route("/")
def trangchu():
    kw = request.args.get("kw")
    products = dao.loadproducts(kw)
    return render_template('index.html', products=products)


@app.route('/register', methods=['get', 'post'])
def user_register():
    navbaritems = dao.loadnavbaritems()
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
                return redirect(url_for('trangchu'))
            else:
                err_msg = 'Mat Khau KHONG Khop!!!'

        except Exception as ex:
            err_msg = 'He thong dang co loi !!!' + str(ex)
    return render_template('register.html', err_msg=err_msg)


@app.context_processor
def common_response():
    return {
        'navbaritems': dao.loadnavbaritems()
    }


if __name__ == "__main__":
    app.run(debug=True)
