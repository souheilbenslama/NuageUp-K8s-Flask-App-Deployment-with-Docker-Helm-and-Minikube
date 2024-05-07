from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/hello/<name>")
def hello_name(name):
    return createhello(name)


def createhello( name ):
    if name:
        return f"Hello, {escape(name)}!"
    return "Hello World !"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/healthz")
def health_check():
    return 'OK', 200

@app.route("/ready")
def ready_check():
    return 'OK', 200


if __name__ == "__main__":
    app.run(debug=True)