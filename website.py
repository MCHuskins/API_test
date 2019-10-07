from flask import Flask
import forecast as ds
app = Flask(__name__)

@app.route("/")
def hello():
    results = ds.get_forecast_data("41.619549", "-93.598022")
    return results["summary"]

@app.route("/another/endpoint")
def secret_hello():
    return "You've found a secret endpoint!"

if __name__ == "__main__":
    app.run()
