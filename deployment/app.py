from joblib import load
import pandas as pd
from flask import Flask, jsonify, request
import requests
from joblib import load
import pandas as pd


app = Flask(__name__)

mymodule = load('pipe.joblib', mmap_mode='r')

@app.route("/predict", methods = ["GET"])
def predict():

    data = request.args
    df = pd.DataFrame([data])
    preds = mymodule.predict(df)

    if predict is not None: 
        result = {"prediction": preds[0]}
        return jsonify(result), 200
    else:
        return " error request", 400
        

if __name__ == '__main__':
    app.run(debug = True)