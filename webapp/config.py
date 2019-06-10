import os

basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = 'Moscow,Russia'
WEATHER_API_KEY = '04a4a202c86048e19bb74339192905'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')