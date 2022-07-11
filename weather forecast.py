import requests #библиотека для поиска информации в интернете

print("Прогноз погоды. Автор программы Орлов Артём. 2022 год")
print("----------")

appid = "f5c754c48978be0d9fb66dc2871ef65c" #заходим в систему под нашим айпиайди

city_id_sergievposad = 496638 #указываем номер нужного нам города, чтобы узнать прогноз погоды в нём
print("Погода в Сергиевом Посаде, Россия")

try: 
    res = requests.get("http://api.openweathermap.org/data/2.5/weather", #выполняем наш поиск, задавая нужные параметры
                 params={'id': city_id_sergievposad, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json() #с этого файла мы будем брать информацию
    print("осадки:", data['weather'][0]['description']) 
    print("температура:", data['main']['temp'], "°C") #также для удобства можно указать единицы измерения
    print("скорость ветра:", data['wind']['speed'], "м/с")
    print("атмосферное давление:", data['main']['pressure'] * 75/100) #пребразуем наши данные в понятный формат
    print("влажность:", data['main']['humidity'], "%") 
    print("облачность:", data ['clouds']['all'], "%")
except Exception as e: #если какой-то параметр программе понятен не будет, нам высветится ошибка
    print("Исключение:", e)
    pass

print("----------")
#далее мы будем делать похожее с разными городами
city_id_moscow = 524901
print("Погода в Москве, Россия")

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id_moscow, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("осадки:", data['weather'][0]['description'])
    print("температура:", data['main']['temp'], "°C")
    print("скорость ветра:", data['wind']['speed'], "м/с")
    print("атмосферное давление:", data['main']['pressure'] * 75 /100)
    print("влажность:", data['main']['humidity'], "%")
    print("облачность:", data ['clouds']['all'], "%")
except Exception as e:
    print("Исключение:", e)
    pass

print("----------")
    
city_id_nizhnynovgorod = 520555
print("Погода в Нижнем Новгороде, Россия")

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id_nizhnynovgorod, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("осадки:", data['weather'][0]['description'])
    print("температура:", data['main']['temp'], "°C")
    print("скорость ветра:", data['wind']['speed'], "м/с")
    print("атмосферное давление:", data['main']['pressure'] * 75 /100)
    print("влажность:", data['main']['humidity'], "%")
    print("облачность:", data ['clouds']['all'], "%")
except Exception as e:
    print("Исключение:", e)
    pass

print("----------")

city_id_saintpetersburg = 498817
print("Погода в Санкт-Петербурге, Россия")

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id_saintpetersburg, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("осадки:", data['weather'][0]['description'])
    print("температура:", data['main']['temp'], "°C")
    print("скорость ветра:", data['wind']['speed'], "м/с")
    print("атмосферное давление:", data['main']['pressure'] * 75/100)
    print("влажность:", data['main']['humidity'], "%")
    print("облачность:", data ['clouds']['all'], "%")
except Exception as e:
    print("Исключение:", e)
    pass

print("----------")

city_id_yerevan = 616052
print("Погода в Ереване, Армения")

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id_yerevan, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("осадки:", data['weather'][0]['description'])
    print("температура:", data['main']['temp'], "°C")
    print("скорость ветра:", data['wind']['speed'], "м/с")
    print("атмосферное давление:", data['main']['pressure'] *75/100)
    print("влажность:", data['main']['humidity'], "%")
    print("облачность:", data ['clouds']['all'], "%")
except Exception as e:
    print("Исключение:", e)
    pass
print("----------")
