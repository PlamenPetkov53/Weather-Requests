import requests
import json
import random
import re

api_key = "11f4d17a26f59a54f5685e9bf59ef4fe"
coldest_city=[]
new_list =[]
cities =  ['Tokyo', 'Delhi', 'Shanghai', 'Cairo', 'Monaco', 'Mumbai', 'Karachi', 'Osaka', 'Istanbul', 'Lago', 'Moscow', 'Lahore', 'Bangalore', 'Paris', 'Bogota', 'Jakarta', 'Lima', 'Seoul', 'London', 'Chicago', 'Madrid', 'Toronto', 'Sofia', 'Plovdiv', 'Burgas']
new_list += random.sample(cities, 5)



for x in new_list:
        url_five = f"http://api.openweathermap.org/data/2.5/weather?q={x}&appid={api_key}&units=metric"
        response_five = requests.get(url_five)
        data_five = json.loads(response_five.text)
        if "message" in data_five:
            city_not_found = data_five["message"]
            print(city_not_found)
        else:
            print("---------------------------------------------------------------")
            print(f"{data_five['name']}: ")
            coldest_city.append(data_five['main']['temp'])
            print(f"Current temperature is:  {round(data_five['main']['temp'])} degrees celsius")
            print(f"Current humidity is: {data_five['main']['humidity']} %")

            for i in data_five["weather"]:
                print(f"The sky is: {i['description']}")
print("---------------------------------------------------------------")
print(f"Minimum temperature is: {round(min(coldest_city))} degrees celsius")
print(f"Average temperature is: {round(sum(coldest_city) / len(coldest_city))} degrees celsius")

user_input = re.findall(r"[\w']+", input())


url = f"http://api.openweathermap.org/data/2.5/weather?q={user_input[0]}&appid={api_key}&units=metric"
response = requests.get(url)
data = json.loads(response.text)
if "message" in data:
        city_not_found = data["message"]
        print(city_not_found)
else:
        print("---------------------------------------------------------------")
        print(f"{data['name']}: ")
        print(f"Current temperature is:  {round(data['main']['temp'])} degrees celsius")
        print(f"Current humidity is: {data['main']['humidity']} %")
        for i in data["weather"]:
            print(f"The sky is: {i['description']}")






