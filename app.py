from flask import Flask, request, render_template, redirect, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        data = request.form["upiid"]
        return redirect(f"/{data}")


@app.route("/<upi>")
def upi_route(upi):
    if '@' in upi:
        return render_template("upi.html", upi=upi)
    else:
        return jsonify({"error": "something went wrong"})


@app.route("/<upi>/<int:amount>")
def amount_payment(upi, amount):
    if '@' in upi:
        if type(amount) is int:
            return render_template('upi.html', upi=upi, amount=amount)
        else:
            return jsonify({"error": f"amount should be integer and not, {type(amount)}"})
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
