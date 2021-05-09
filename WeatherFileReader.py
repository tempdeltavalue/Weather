import os
import glob
import json

class Weather:
    def __init__(self, json_obj):
        self.lat = json_obj["lat"]
        self.lon = json_obj["lon"]
        self.current = json_obj["current"]
        self.minutely = json_obj["minutely"]
        self.hourly = json_obj["hourly"]
        self.daily = json_obj["daily"]

class WeatherFileReader:
    def __init__(self, path):
        print("VOVA")

        self.path = path

    def read_files(self):
        paths = glob.glob(os.path.join(self.path, "*"))
        dict_r = {}
        for date_path in paths:
            json_paths = glob.glob(os.path.join(date_path, "*"))
            for json_path in json_paths:
                with open(json_path) as file:
                    json_obj = json.load(file)
                    weather = Weather(json_obj)
                    comps = json_path.split("/")[-1].split("_")
                    w_loc_id = comps[5]

                    if w_loc_id not in dict_r:
                        dict_r[w_loc_id] = []

                    dict_r[w_loc_id].append(weather)
                    print(json_path)
                    print(comps)



                    print(json_path.split("/")[-1].split("_")[5])
                    print(weather)


if __name__ == "__main__":
    f_r = WeatherFileReader("WeatherData")
    f_r.read_files()
