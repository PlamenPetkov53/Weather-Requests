from flask import Flask, render_template, request
import requests
import re
import json

app=Flask(__name__)

@app.route("/", methods=['POST', 'GET'])

def RequestWeather():
    api_key = "11f4d17a26f59a54f5685e9bf59ef4fe"
    coldest_city=[]
    input = ""
    city_not_found = ""
    name_of_city =""
    current_humidity=""
    current_temp = ""
    min_temp = ""
    average_temp = ""
    sky = ""
    
    if request.method == 'POST' and  'Input' in request.form:
        first  = str(request.form.get('Input'))
       user_input = re.findall(r"[\w']+", first
       
        if len(user_input) == 5:

            for x in user_input:
                            url_five = f"http://api.openweathermap.org/data/2.5/weather?q={x}&appid={api_key}&units=metric"
                            response_five = requests.get(url_five)
                            data_five = json.loads(response_five.text)
                            if "message" in data_five:
                                city_not_found = data_five["message"]
                            else:
        
                                name_of_city = data_five['name']
                                coldest_city.append(data_five['main']['temp'])
                             
                                current_temp= round(data_five['main']['temp']
                            
                                current_humidity=data_five['main']['humidity']

                                for i in data_five["weather"]:
                                    
                                    sky=i['description']
            
            min_temp = round(min(coldest_city))
            average_temp=round(sum(coldest_city) / len(coldest_city))


      
    return render_template("index.html", city_not_found=city_not_found, name_of_city=name_of_city, current_temp=current_tempр, current_humidity=current_humidity, sky=sky, min_temp=min_temp, average_temp=average_temp )
                        



        

