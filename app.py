from flask import Flask
from flask import render_template, jsonify
import requests
app = Flask(__name__)


@app.route("/top_stories/")
def top_stories():
    response = requests.get("http://api.nytimes.com/svc/topstories/v1/home.json?api-key=ba5407bdbf571895b000d0faa7948cbe:2:72232947")
    return jsonify(response.json(), status=200)


@app.route("/search/")
def search():
    results = requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/20/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/40/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/60/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/80/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/100/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/120/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/140/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/160/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/180/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/220/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/240/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/260/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/280/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/300/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/320/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/340/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/360/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/380/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/400/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/420/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/440/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/460/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/480/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/500/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/520/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)
    for result in (requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7/540/json?api-key=5833081c31fb947072ec5e9820a498fa:18:72232947").json()['results']):
        results.append(result)

    return jsonify(results=results, status=200)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
