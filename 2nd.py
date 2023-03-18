import requests

city = "Moscow,RU"
appid = "e84dd76c684568b6f05eb8343d3807a4"
realpar = {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid}

res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=realpar)
data = res.json()
#print(res.url)

print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), '°', "> \r\nПогодные условия <", i['weather'][0]['description'], "> \r\nСкорость ветра <", i['wind']['speed'], "м/с > \r\nВидимость <", i['visibility'], "м >")
    print("____________________________")