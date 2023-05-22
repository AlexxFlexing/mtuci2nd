import requests

city = "Moscow,RU"
appid = "filtered"
realpar = {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid}

res = requests.get("http://api.openweathermap.org/data/2.5/weather", params=realpar)
data = res.json()
#print(res.url)

print("Город:", data['name'])
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'], "°")
print("Минимальная температура:", data['main']['temp_min'], "°")
print("Максимальная температура", data['main']['temp_max'], "°")
print("Скорость ветра:", data['wind']['speed'], "м/с")
print("Видимость:", data['visibility'], "м")
