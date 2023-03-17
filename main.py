import requests

city = "Moscow,RU"

#в переменной city находятся 2 аргумента для api call'а
#первая часть переменной отвечает за location name
#чтобы узнать его необходимо провести reverse geocoding


appid = "e84dd76c684568b6f05eb8343d3807a4"
realpar = {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid}

res = requests.get("http://api.openweathermap.org/data/2.5/weather", params=realpar)
data = res.json()
print(res.url)

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed'])