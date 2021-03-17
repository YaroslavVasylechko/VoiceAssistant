import requests

def get_weather(sity):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': {sity}, 'units': 'metric', 'lang': 'en',
                                   'APPID': '8f0092dc76a29defef007ae8be592efb'})
        data = res.json()
        res = (f'Conditions: {data["weather"][0]["description"]}, temperature now: {data["main"]["temp"]}, minimum ' \
              f'temperature: {data["main"]["temp_min"]}, maximum temperature: {data["main"]["temp_max"]}')
        print(res)
        return str(res)
    except Exception as e:
        print("Exception (weather):", e)
        pass

if __name__ == '__main__':
    get_weather('moscow')
