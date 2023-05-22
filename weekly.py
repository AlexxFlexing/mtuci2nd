import requests

city = "Moscow,RU"
appid = "filtered"
realpar = {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid}

res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=realpar)
data = res.json()
#print(res.url)
print("Прогноз погоды на неделю:")
for i in data['list']:
    #print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), '°', "> \r\nПогодные условия <", i['weather'][0]['description'], "> \r\nСкорость ветра <", i['wind']['speed'], "м/с > \r\nВидимость <", i['visibility'], "м >")
    print("Дата <", i['dt_txt'], ">")
    print("Температура <", '{0:+0.0f}'.format(i['main']['temp']), "° >")
    print("Погодные условия <", i['weather'][0]['description'], ">")
    print("Скорость ветра <", i['wind']['speed'], "м/с >")
    print("Видимость <", i['visibility'], "м >")
    print("____________________________")
