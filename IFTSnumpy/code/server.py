import flask
import os
import json

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("upload.html")


@app.route("/uploader", methods=["POST"])
def uploader():
    # uploaded = flask.request.files["file"]
    uploaded = flask.request.files.getlist("file")
    # print(uploaded.save(f"uploaded/{uploaded.filename}"))
    for f in uploaded:
        f.save(f"uploads/{f.filename}")
    return "Caricamento avvenuto con successo"


@app.route("/create_folder/<path:path>", methods=["POST"])
def create_folder(path):
    print(path)
    if os.path.exists(f"uploads/{path}"):
        return json.dumps({"success": False, "error": "folder already existing"})
    else:
        os.mkdir(f"uploads/{path}")
        return json.dumps({"success": True, "folder": path})


@app.route("/folders/")
def folders():
    return flask.render_template("folders.html")


@app.route("/read_folder", methods=["POST"])
def read_folder():
    folder = flask.request.get_json()["folder"]
    if os.path.exists(f"uploads/{folder}"):
        folder_content = os.listdir(f"uploads/{folder}")
        folders_to_show = []
        files_to_show = []
        for x in folder_content:
            i = f".../{folder}" + x
            x = f"uploads/{folder}" + x

            if os.path.isdir(x):
                folders_to_show += [x]
            if os.path.isfile(x):
                files_to_show += [x]
        return json.dumps(
            {"success": True, "folders": folders_to_show, "files": files_to_show}
        )
    else:
        return json.dumps({"success": True, "error": "folder does not exist"})


@app.route("/get_file/<path:path>")
def get_file(path):
    return flask.send_file(f"../uploads/{path}")


"""
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
"""

app.run("0.0.0.0", 8080, True)
