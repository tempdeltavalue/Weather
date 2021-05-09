import requests
import datetime
import json
import os
from random import seed
from random import random, uniform
import time
# seed random number generator
seed(1)

STORED_DATA_PLACE = "WeatherData"

class WeatherAPI:
    def __init__(self):
        self.URL_API_KEY = ""
        self.URL_LATITUDE = "50.512390"
        self.URL_LONGITUDE = "25.607000"
        self.URL_GET_ONE_CALL = ""
        self.URL_BASE = "https://api.openweathermap.org/data/2.5"


    def buildURL(self):
        URL_GET_ONE_CALL = "/onecall?lat=" + self.URL_LATITUDE + "&lon=" + self.URL_LONGITUDE + "&units=imperial" + "&appid=" + self.URL_API_KEY
        return self.URL_BASE + URL_GET_ONE_CALL

    def request_weather(self, lat, long):
        self.URL_LATITUDE = str(lat)
        self.URL_LONGITUDE = str(long)

        url = self.buildURL()
        return requests.post(url)


def create_folder_name():
    now = datetime.datetime.now()
    folder_name = '_'.join([str(now.year),
                            str(now.month),
                            str(now.day),
                            str(now.hour),
                            str(now.minute)])
    return folder_name



def weather_random_area_search(generated_coords):
    weatherAPI = WeatherAPI()

    date_folder_name = create_folder_name()
    date_folder_path = os.path.join(STORED_DATA_PLACE, date_folder_name)
    if os.path.exists(date_folder_path) is False:
        print("\n FOLDER CREATED \n")
        os.mkdir(date_folder_path)

    for index, coord in enumerate(generated_coords):
        print(coord)

        x = weatherAPI.request_weather(coord[0], coord[1])

        json_obj = json.loads(x.text)
        # print("json_obj keys", json_obj.keys())
        lat = json_obj["lat"]
        lon = json_obj["lon"]
        current = json_obj["current"]
        print("current", current)

        minutely = json_obj["minutely"]
        print("minutely", len(minutely), minutely)
        hourly = json_obj["hourly"]
        print("hourly", len(hourly), hourly)

        daily = json_obj["daily"]
        #
        # print("hourly", len(hourly), hourly)
        # print("daily", len(daily), daily)

        json_path = os.path.join(date_folder_path, 'data_{}__{}.json'.format(index, coord))
        with open(json_path, 'w') as outfile:
            json.dump(json_obj, outfile)
            print("storing finished")





if __name__ == "__main__":
    weatherAPI = WeatherAPI()
    lat, long = (50.512390, 25.607000)
    delta_side = 20
    n = 400

    generated_coords = []
    for i in range(n):
        new_lat = uniform(lat-delta_side, lat+delta_side)
        new_long = uniform(long-delta_side, long+delta_side)
        generated_coords.append([new_lat, new_long])

    while True:
        # Code executed here
        print("Vova \n \n")
        weather_random_area_search(generated_coords)
        time.sleep(60 * 60)

