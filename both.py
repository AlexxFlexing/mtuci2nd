import requests
print("Выберите тип прогноза", "\r\nВведите 1 для просмотра текущей погоды или 2 для просмотра прогноза погоды на неделю")
choiceNum = int(input())

city = "Moscow,RU"
appid = "e84dd76c684568b6f05eb8343d3807a4"
realpar = {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid}

if choiceNum == 1:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather", params=realpar)
    data = res.json()
    # print(res.url)

    print("Город:", data['name'])
    print("Погодные условия:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'], "°")
    print("Минимальная температура:", data['main']['temp_min'], "°")
    print("Максимальная температура", data['main']['temp_max'], "°")
    print("Скорость ветра:", data['wind']['speed'], "м/с")
    print("Видимость:", data['visibility'], "м")

if choiceNum == 2:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=realpar)
    data = res.json()
    # print(res.url)
    print("Прогноз погоды на неделю:")
    for i in data['list']:
        # print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), '°', "> \r\nПогодные условия <", i['weather'][0]['description'], "> \r\nСкорость ветра <", i['wind']['speed'], "м/с > \r\nВидимость <", i['visibility'], "м >")
        print("Дата <", i['dt_txt'], ">")
        print("Температура <", '{0:+0.0f}'.format(i['main']['temp']), "° >")
        print("Погодные условия <", i['weather'][0]['description'], ">")
        print("Скорость ветра <", i['wind']['speed'], "м/с >")
        print("Видимость <", i['visibility'], "м >")
        print("____________________________")

if choiceNum !=1 and choiceNum != 2:
    print("Введите значение ПРЕДЛОЖЕННОЕ в начале программы")