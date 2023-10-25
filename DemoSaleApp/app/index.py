from flask import Flask, render_template, request
import dao
app = Flask("__main__")


@app.route("/")
def trangchu():
    navbaritems = dao.loaditemnavbar()
    kw = request.args.get("kw")
    phones = dao.loadphoneitem(kw)
    return render_template('index.html', navbaritems=navbaritems, phones=phones)
if __name__ == "__main__":
    app.run(debug=True)
