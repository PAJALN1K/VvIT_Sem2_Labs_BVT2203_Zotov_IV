import requests


city = 'Moscow'
appid = 'some_password_string'


res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Видимость:", data['visibility'])
print("Скорость ветра:", data['wind']['speed'])
print()

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:\n\n")
for i in data['list']:
    print("Дата <", i['dt_txt'], ">"
          "\nТемпература: <", '{0:+3.0f}'.format(i['main']['temp']), ">"
          "\nПогодные условия: <", i['weather'][0]['description'], ">",
          "\nВидимость: <", i['visibility'], ">",
          "\nСкорость ветра: <", i['wind']['speed'], ">", sep='')
    print("____________________________")
