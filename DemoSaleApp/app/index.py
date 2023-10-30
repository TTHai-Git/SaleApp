from flask import render_template, request, jsonify
import dao
from app import app


@app.route("/")
def trangchu():
    navbaritems = dao.loadnavbaritems()
    kw = request.args.get("kw")
    products = dao.loadproducts(kw)
    return render_template('index.html', navbaritems=navbaritems, products=products)


if __name__ == "__main__":
    app.run(debug=True)
