from tkinter import *
import  tkinter as tk
import requests
import json
import random
with open (r"C:\Users\Plamen\Desktop\django\WR\WR\city-city_id.json", encoding='utf-8-sig') as f:
    data = json.load(f)
import re
class WeatherRequests:

    def search_for_one_city(self, user_input, t4, t5, t6, t7, t8, t9):
        s = ''.join(user_input)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={s}&appid=11f4d17a26f59a54f5685e9bf59ef4fe&units=metric"
        response = requests.get(url)
        data = json.loads(response.text)

        if "message" in data:
            city_not_found = data["message"]
            t4.insert(END, str(f"{city_not_found}   "))
        else:
            name_of_city = data['name']
            t4.insert(END, str(f"{name_of_city}  "))
            current_temperature = round(data['main']['temp'])
            t5.insert(END, str(f"{current_temperature} "))
            current_humidity = data['main']['humidity']
            t6.insert(END, str(f"{current_humidity}  "))

            for i in data["weather"]:
                sky_is = i['description']
                # maybe need aray indx

            t7.insert(END, str(f"{sky_is}  "))



    def search_for_five_cities (self, user_input, t4, t5, t6, t7, t8, t9):
        coldest_city = []
        new_list = []
        for x in range(5):
            new_list.append(random.choice(list(data.keys())))

        for x in new_list:
            url_five = f"http://api.openweathermap.org/data/2.5/weather?q={x}&appid=11f4d17a26f59a54f5685e9bf59ef4fe&units=metric"
            response_five = requests.get(url_five)
            data_five = json.loads(response_five.text)

            if "message" in data_five:
                city_not_found = data_five["message"]
                t4.insert(END, str(f"{city_not_found}   "))
            else:
                name_of_city = data_five['name']
                t4.insert(END, str(f"{name_of_city},  "))
                coldest_city.append(data_five['main']['temp'])
                current_temperature = round(data_five['main']['temp'])
                t5.insert(END, str(f"{current_temperature},  "))
                current_humidity = data_five['main']['humidity']
                t6.insert(END, str(f"{current_humidity},  "))

                for i in data_five["weather"]:
                    sky_is = i['description']
                    t7.insert(END, str(f"{sky_is},   "))

                    #maybe need aray indx

        mini_temp = round(min(coldest_city))
        t8.insert(END, str(f"{mini_temp}  "))
        average_temp = round(sum(coldest_city) / len(coldest_city))
        t9.insert(END, str(f"{average_temp}  "))





