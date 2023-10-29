from flask import render_template, request
import dao
from app import app

@app.route("/")
def trangchu():
    navbaritems = dao.loaditemnavbar()
    kw = request.args.get("kw")
    phones = dao.loadphoneitem(kw)
    return render_template('index.html', navbaritems=navbaritems, phones=phones)

if __name__ == "__main__":
    app.run(debug=True)
