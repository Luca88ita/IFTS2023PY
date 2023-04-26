import flask
import json

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


@app.route("/calcolatrice")
def calcolatrice():
    return flask.render_template("calcolatrice.html")


@app.route("/calcolatriceAPI", methods=["POST", "GET"])
def calcolatriceAPI():
    GET = flask.request.args  # per leggere i parametri GET
    POST = flask.request.get_data()  # per leggere i parametri POST
    JSON = flask.request.get_json()  # per leggere i parametri POST JSON

    print(JSON)

    num1 = float(JSON["num1"])
    num2 = float(JSON["num2"])

    result = num1 + num2

    return json.dumps(result)


app.run("0.0.0.0", 8080, True)
