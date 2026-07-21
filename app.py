from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chickens")
@app.route("/chica")
@app.route("/chickenwhatever")
def chickens():
    return render_template("chickens.html")

@app.route("/pandas")
@app.route("/pandu")
@app.route("/pandawhatever")
def pandas():
    return render_template("pandas.html")

@app.route("/cats")
@app.route("/kitty")
@app.route("/catwhatever")
def cats():
    return render_template("cats.html")

if __name__ == "__main__":
    app.run(port=5678)
    
