import flask
import torch
import os
import json

app = flask.Flask(__name__)
model = torch.jit.load("traced_conv.pt")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    image = flask.request.get_json()["image"]
    image = torch.tensor(image)
    
    y = model(image)
    print(y.argmax())
    return "ciao"



app.run("0.0.0.0", 5000, True)
