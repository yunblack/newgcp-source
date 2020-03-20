from flask import Flask

import requests
import json
import datetime

Date = []
City = []
Low_Temp = []
High_Temp = []
Avg_Temp = []
Humidity = []
Pressure = []
Wind = []

app = Flask(__name__)

def weatherAPI():
    now = datetime.datetime.now()
    apikey = "474d59dd890c4108f62f192e0c6fce01"
    cities = ["Seoul,KR"]  ##
    api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

    k2c = lambda k: k - 273.15

    for name in cities:
        url = api.format(city=name, key=apikey)
        r = requests.get(url)
        data = json.loads(r.text)

        print("City Name : ", data["name"])
        print("Date : ", now)
        print("Weather : ", data["weather"][0]["description"])
        print("Lowest Temperature : ", k2c(data["main"]["temp_min"]))
        print("Highest Temperature : ", k2c(data["main"]["temp_max"]))
        print("Average Temperature : ", round(k2c(data["main"]["temp"])), 2)
        print("Humidity : ", data["main"]["humidity"])
        print("Pressure : ", data["main"]["pressure"])
        print("Wind : ", data["wind"]["speed"])
        print("")

def main():
    weatherAPI()


if __name__ == '__main__':
    main()
    app.run(host='127.0.0.1', port=8080, debug=True)
