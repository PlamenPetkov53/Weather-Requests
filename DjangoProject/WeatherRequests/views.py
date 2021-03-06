from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import RequestedCities
with open (r"C:\Users\Plamen\Desktop\django\WR\WR\city-city_id.json", encoding='utf-8-sig') as f:
    data = json.load(f)
import os
import requests
import re
import random

#For START UP Random Generator
def input (request):
    x = " "
    api_key = "11f4d17a26f59a54f5685e9bf59ef4fe"
    new_list =[]
    for x in range(5):
        new_list.append(random.choice(list(data.keys())))

    coldest_city=[]
    input = ""
    city_not_found = ""
    name_of_city =[]
    current_humidity=[]
    current_temp = []
    min_temp = ""
    average_temp = ""
    sky = []
    last_ten = RequestedCities.objects.all().order_by('-id')[:10]
    last_ten1 = reversed(last_ten)
    


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
    context= {'result': last_ten1, 'name': name_of_city, 'cuurent_temp': current_temp, 'current_humidity': current_humidity, 'Sky_Descp': sky, 'min_temp': min_temp, 'average_temp': average_temp, 'city_not_found': city_not_found}
    return render(request, 'form.html', context)
#For User Input
def index (request):
     city_not_found = None
     name_of_city = None
     current_humidity = None
     current_temp = None
     sky = None
     smth = None
     


     num1 = request.GET['input']
     api_key = "11f4d17a26f59a54f5685e9bf59ef4fe"
     #user_input = re.findall(r"[\w']+", num1)
     url = f"http://api.openweathermap.org/data/2.5/weather?q={num1}&appid={api_key}&units=metric"
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


     WR_instance = RequestedCities.objects.create(name_of_city=name_of_city, current_temp=current_temp, current_humidity=current_humidity,sky_cond = sky)
     WR_instance.save_base()
     WR_instance.save()   
     context= {'reversed_list': smth, 'name_of_city_input': name_of_city, 'current_temp_input': current_temp, 'current_humidity_input': current_humidity, 'Sky_Descp_input': sky, 'city_not_found_input': city_not_found}
     return render(request, 'form.html', context)

def table(request):
    last_ten = RequestedCities.objects.all().order_by('-id')[:10]
    last_ten1 = reversed(last_ten)
    context= {'table': last_ten1}
    return render(request, 'form.html', context)

def Compare(request):
    num1 = request.GET['input_first']
    data1 = RequestedCities.objects.filter(id=int(num1)).values()

    num2 = request.GET['input_second']
    data2 = RequestedCities.objects.filter(id=int(num2)).values()
    context = {"id1": data1, "id2": data2}
    return render(request, 'form.html', context)
