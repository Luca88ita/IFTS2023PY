import flask

app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    answer = ""
    for i in range(10):
        answer += f"<h{i}>{i}</h{i}>"
    return answer


# con @ definisco un decorator che aggiunge una funzionalità ad una funzione
@app.route("/pagina0")
def pagina0():
    return "Ciao, sono Luca"


@app.route("/pagina1")
def pagina1():
    with open("code/pagina1.html") as file:
        content = file.read()
    return content


@app.route("/pagina2")
def pagina2():
    return flask.render_template("pagina2.html")


@app.route("/calcolatrice", methods=["POST", "GET"])
def calcolatrice():
    return flask.render_template("calcolatrice.html")


app.run("0.0.0.0", 8080, True)
