# Imports
from config import user, pgs, url
from datetime import datetime
from sqlalchemy import create_engine
from time import sleep
import pandas as pd
import requests

# Create a request function with a clever name
def weather_getter(url):
    response = requests.get(url).json()
    df = pd.DataFrame([[datetime.now(), response['main']['humidity'], response['clouds']['all']]],
                      columns = ['date','humidity','clouds'])
    return df

# Infinite loop to collect and store weather data every 30 minutes
while True:
    # SQL engine
    engine = create_engine(pgs)

    with engine.connect() as conn:
        # Request weather data
        df = weather_getter(url)

        # Upload weather data
        df.to_sql("weather_log", conn, schema = f"{user}/cbus_temps", index = False, if_exists = 'append')

    # Wait 30 minutes
    sleep(60 * 30)
