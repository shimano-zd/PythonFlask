from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def homepage():

    return render_template("index.html", jsonWeather=getWeather(3186952))
 
@app.route("/test")
def test():
    return render_template("test.html")

@app.route('/weather')
def index():
    # 2643743 London, 3186952 Zadar
    return city(3186952)

@app.route('/<id>')
def city(id):
    parameters = { 'appid': '7f1839b423ed0ec9c2c366cab3867ca2',
    'id': id, 'units': 'metric', 'lang': 'hr' }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    url2 = 'https://api.openweathermap.org/data/2.5/forecast'
    response = requests.get(url, params=parameters)
    response2 = requests.get(url2, params=parameters)
    
    jsonWeather = response.json()
    jsonForecast = response2.json()
    
    dt = datetime.utcfromtimestamp( jsonWeather['dt'] )
    now = datetime.now()
    return render_template('weather.html', jsonWeather=jsonWeather, jsonForecast=jsonForecast, 
        dt=dt, now=now)


def getWeather(id):

    parameters = { 'appid': '7f1839b423ed0ec9c2c366cab3867ca2',
    'id': id, 'units': 'metric', 'lang': 'hr' }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    
    response = requests.get(url, params=parameters)
    
    jsonWeather = response.json()
    
    return jsonWeather

if __name__ == "__main__":
    app.run(debug=True)