import flask
import json

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/static/<path:path>")
def static_files(path):
    return flask.send_from_directory("static", path)


@app.route("/purchase", methods=["POST", "GET"])
def purchase():
    cart = flask.request.get_json()
    for item in cart:
        print(item)
    return json.dumps({"success": True})


@app.route("/login")
def login():
    nome = flask.request.args.get("nome", "")
    if nome == "luca":
        risposta = flask.make_response("benvenuto")
        risposta.set_cookie("accesso", "true")
    else:
        risposta = flask.make_response("nome utente non trovato")
    return risposta


@app.route("/verification")
def verification():
    return "ciao"


@app.route("/attacco")
def attacco():
    return flask.render_template("attacco.html")


@app.route("/tesoro")
def tesoro():
    accesso = flask.request.cookies.get("accesso", "false")
    if accesso == "true":
        risposta = flask.make_response("OnePiece")
    elif accesso == "false":
        risposta = flask.make_response("bloccato")
    else:
        risposta = flask.make_response("sei un attaccante")
    risposta.set_cookie("accesso", "false")
    return risposta


app.run("0.0.0.0", 8080, True)
