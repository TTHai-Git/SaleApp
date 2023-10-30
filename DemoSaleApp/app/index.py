from flask import render_template, request, jsonify
import dao
from app import app

@app.route("/")
def trangchu():
    navbaritems = dao.loaditemnavbar()
    kw = request.args.get("kw")
    phones = dao.loadphoneitem(kw)
    return render_template('index.html', navbaritems=navbaritems, phones=phones)

@app.route("/category")
def category():
    dshang = dao.hienthidanhsach()
    for row in dshang.scalar_subquery():
        print(f"{row.id} {row.name}")


if __name__ == "__main__":
    app.run(debug=True)
