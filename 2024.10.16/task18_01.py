import requests #импорт библиотеки requests

url = 'http://api.forismatic.com/api/1.0/' #объявление и инициализация переменной url
payload  = {'method': 'getQuote', 'format': 'json', 'lang': 'ru'} #создание словаря
res = requests.get(url, params=payload) #объявление переменной и инициализация еётрезультатом работы функции requests.get 

data = res.json() ##объявление переменной и инициализация еётрезультатом работы функции res.json 

print(data) #вывод переменной data на экран