from enum import Enum
import requests, json
import datetime as dt
import pandas as pd

API_KEY = "ef22798ad351d3d9e8de0210e00aa6bc"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
UNITS = "&units=imperial"

class Weather(Enum):
    BAD = -1
    NEUTRAL = 0
    GOOD = 1

def assign_enum(weather):
    """Returns: a Weather enum based on the following mapping rule:
        Sunny or >5 degrees warmer than tomorrow  =>  Weather.GOOD
        Precipitating or >5 degrees cooler than tomorrow  =>  Weather.BAD
        Otherwise  =>  Weather.NEUTRAL
    Requires:  dictionary containing today's high temperature, tomorrow's high
    temperature, and today's weather description. Could also pass in None."""
    if weather is None:
        return Weather.NEUTRAL
    else:
        temp_diff = weather['tmrw_high'] - weather['today_high']
        if weather['today_desc'] == 'Clear' or temp_diff <= -5:
            return Weather.GOOD
        elif weather['today_desc'] in ['Thunderstorm','Drizzle','Rain'] or temp_diff >= 5:
            return Weather.BAD
        else:
            return Weather.NEUTRAL

def get_weather(zip):
    """Returns: a dictionary containing today's high temperature, tomorrow's high
    temperature, and today's weather description. If that data cannot be accessed,
    it will return None.
    Requires: a zip code as a string
    Note: the method for determining the weather description is to use the most
    common descriptor throughout the day, defined as the hours from 8:00
    to 20:00, inclusive. However, if the data given for today exists outside this
    range, it will use any data given regardless of the hour. On a tie for the most
    common, this function just selects the first one."""
    complete_url = BASE_URL + "appid=" + API_KEY + "&zip=" + zip + UNITS
    response = requests.get(complete_url)
    d = response.json()

    if d['cod'] == '200':
        lst = []
        for data_point in d['list']:
            time = dt.datetime.fromtimestamp(data_point['dt'])
            temp = data_point['main']['temp']
            desc = data_point['weather'][0]['main']
            lst.append({'datetime': time, 'temp': temp, 'desc': desc})
        table = pd.DataFrame(lst, columns=['datetime','temp','desc'])

        #extract the date and time to use for filtering
        f1 = lambda row: row['datetime'].date()
        f2 = lambda row: row['datetime'].time()
        table['day'] = table.apply(f1, axis=1)
        table['time'] = table.apply(f2, axis=1)

        today = table.loc[0,'day']
        tmrw = today + dt.timedelta(1)

        today_high = table[table['day'] == today]['temp'].max()
        tmrw_high = table[table['day'] == tmrw]['temp'].max()

        daytime = table[(table['time'] >= dt.time(8)) & (table['time'] <= dt.time(20))]
        if daytime[daytime['day'] == today].shape[0] > 0:
            today_desc = daytime[daytime['day'] == today]['desc'].mode()[0]
        else:
            today_desc = table[table['day'] == today]['desc'].mode()[0]

        return {'today_high': today_high, 'tmrw_high': tmrw_high, 'today_desc': today_desc}
    else:
        return None
