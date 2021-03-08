from django.shortcuts import render
from django.http import HttpResponse
import os
import requests
import re
import random
import json
#For START UP Random Generator
def input (request):
    api_key = "11f4d17a26f59a54f5685e9bf59ef4fe"
    new_list =[]
    cities =  ['Tokyo', 'Delhi', 'Shanghai', 'Cairo', 'Monaco', 'Mumbai', 'Karachi', 'Osaka', 'Istanbul', 'Lago', 'Moscow', 'Lahore', 'Bangalore', 'Paris', 'Bogota', 'Jakarta', 'Lima', 'Seoul', 'London', 'Chicago', 'Madrid', 'Toronto', 'Sofia', 'Plovdiv', 'Burgas']
    new_list += random.sample(cities, 5)
    a = len(cities)
    coldest_city=[]
    input = ""
    city_not_found = ""
    name_of_city =[]
    current_humidity=[]
    current_temp = []
    min_temp = ""
    average_temp = ""
    sky = []
    for x in new_list:
            url_five = f"http://api.openweathermap.org/data/2.5/weather?q={x}&appid={api_key}&units=metric"
            response_five = requests.get(url_five)
            data_five = json.loads(response_five.text)
            if "message" in data_five:
                city_not_found = data_five["message"]
            else:
        
                name_of_city.append(data_five['name'])
                coldest_city.append(data_five['main']['temp'])
                             
                current_temp.append(round(data_five['main']['temp']))
                            
                current_humidity.append(data_five['main']['humidity'])
                               

                for i in data_five["weather"]:
                                    
                    sky.append(i['description'])
    min_temp = round(min(coldest_city))
    average_temp = round(sum(coldest_city) / len(coldest_city))
    return render(request, 'form.html', {"result": [city_not_found, name_of_city, current_temp, current_humidity, sky, min_temp, average_temp]})

#For User Input
def index (request):
     city_not_found = ""
     name_of_city = ""
     current_humidity=""
     current_temp = ""
     sky = ""




     num1 = request.GET['input']
     api_key = "11f4d17a26f59a54f5685e9bf59ef4fe"
     user_input = re.findall(r"[\w']+", num1)
     url = f"http://api.openweathermap.org/data/2.5/weather?q={user_input[0]}&appid={api_key}&units=metric"
     response = requests.get(url)
     data = json.loads(response.text)
     if "message" in data:
          city_not_found = data["message"]
                    
     else:
          name_of_city = data['name']
          current_temp = round(data['main']['temp'])
          current_humidity = data['main']['humidity']
          for i in data["weather"]:
               sky = i['description']
     return render(request, 'form.html', {"smth":[city_not_found, name_of_city, current_temp, current_humidity, sky]})
