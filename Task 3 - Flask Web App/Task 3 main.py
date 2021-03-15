from flask import Flask, render_template, request
import requests
import re
import random
import json

app=Flask(__name__)

@app.route("/", methods=['POST', 'GET'])

def RequestWeather():
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
    ct_not_found = None 
    nm_inpt = None
    ct_inpt = None
    ch_inpt = None
    sky_inpt = None
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
    
    if request.method == 'POST' and  'Input' in request.form:
        name_of_city.clear
        current_humidity.clear()
        current_temp.clear()
        sky.clear()
        cities.clear()

        
        first  = str(request.form.get('Input'))
        user_input = re.findall(r"[\w']+", first)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={user_input[0]}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = json.loads(response.text)
        if "message" in data:
            ct_not_found = data["message"]
                    
        else:
            nm_inpt = data['name']
            ct_inpt = round(data['main']['temp'])
            ch_inpt = data['main']['humidity']
            for i in data["weather"]:
                sky_inpt = i['description']
                    


      
    return render_template("index.html" , ct_not_found=ct_not_found, nm_inpt=nm_inpt, ct_inpt=ct_inpt, ch_inpt= ch_inpt, sky_inpt= sky_inpt,  city_not_found=city_not_found, name_of_city=name_of_city, current_temp=current_temp, current_humidity=current_humidity, sky=sky, min_temp=min_temp, average_temp=average_temp, a=a, new_list=new_list )
                        



        

