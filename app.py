from flask import Flask
from flask import render_template, jsonify
import requests
app = Flask(__name__)


@app.route("/search/")
def search():
    response = requests.get("http://api.nytimes.com/svc/topstories/v1/home.json?api-key=ba5407bdbf571895b000d0faa7948cbe:2:72232947")
    return jsonify(response.json(), status=200)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
