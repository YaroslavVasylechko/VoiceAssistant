import requests
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re


def get_weather(country, sity):

    countries = ["Poland", "USA", "Germany"]
    finalCountry = process.extractOne(str(country), countries)
    correct_Country = finalCountry[0]
    print(correct_Country)

    if correct_Country == 'Poland' or country == 'poland':
        polandCities = ["Warsaw", "Lodz", "Krakow", "Wroclaw", "Poznan", "Gdansk", "Szczecin", "Bydgoszcz",
                        "Lublin", "Katowice", "Bialystok", "Gdynia"]
        finalIndex = process.extractOne(str(sity), polandCities)
        correct_city = finalIndex[0]
    elif correct_Country == 'USA' or country == 'usa':
        usaCities = ["New York", "Los Angeles", "Chicago", "Houston",
                     "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
        finalIndex = process.extractOne(str(sity), usaCities)
        correct_city = finalIndex[0]
    elif correct_Country == 'Germany' or country == 'germany':
        usaCities = ["Berlin", "Hamburg", "Munich", "Cologne",
                     "Frankfurt am Main", "Essen", "Stuttgart", "Dortmund", "Dusseldorf", "Bremen"]
        finalIndex = process.extractOne(str(sity), usaCities)
        correct_city = finalIndex[0]
    else:
        return 'You named the country incorrectly'

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': {correct_city}, 'units': 'metric', 'lang': 'en',
                                   'APPID': '8f0092dc76a29defef007ae8be592efb'})
        data = res.json()
        res = (f'City: {data["name"]}, '
               f'Conditions: {data["weather"][0]["description"]}, temperature now: {data["main"]["temp"]}, minimum ' \
               f'temperature: {data["main"]["temp_min"]}, maximum temperature: {data["main"]["temp_max"]}')
        print(res)
        return str(res)
    except Exception as e:
        print("Exception (weather):", e)
        pass


if __name__ == '__main__':
    get_weather('Poland', 'Los Angle')


# def correctCity(uncorrect_country, uncorrect_city):
#     if uncorrect_country == 'Poland' or uncorrect_country == 'poland':
#         polandCities = ["Warsaw", "Lodz", "Krakow", "Wroclaw", "Poznan", "Gdansk", "Szczecin", "Bydgoszcz",
#                         "Lublin", "Katowice", "Bialystok", "Gdynia", "New York", "Los Angeles", "Chicago", "Houston",
#                         "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
#         finalIndex = process.extractOne(str(uncorrect_city), polandCities)
