from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/risnjak")
def risnjak():
    return render_template("risnjak.html", jsonWeather=getWeather(3202104))


def getWeather(id):

    parameters = { 'appid': '7f1839b423ed0ec9c2c366cab3867ca2',
    'id': id, 'units': 'metric', 'lang': 'en' }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    
    response = requests.get(url, params=parameters)
    
    jsonWeather = response.json()
    
    return jsonWeather

if __name__ == "__main__":
    app.run(debug=True)