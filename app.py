from flask import Flask, redirect, url_for
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://www.google.com/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
