import requests
from django.shortcuts import render


def index(request):
    app_id = '16d766135872a5968465617c82c92251'
    url_id = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id

    city = 'London'
    res = requests.get(url_id.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    context = {'info': city_info}

    return render(request, 'weather/index.html', context)
