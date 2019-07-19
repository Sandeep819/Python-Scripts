import json

with open('json_files/mumbai_weather.json') as f:
    json_data = json.load(f)



print("Temparature now in ",city, "is : ",json_data['main']['temp'])
print("Pressure now in ",city, "is : ",json_data['main']['pressure'])
print("Humidity now in ",city, "is : ",json_data['main']['humidity'])
print("Maximum Temparature now in ",city, "is : ",json_data['main']['temp_min'])
print("minimum Temparature now in ",city, "is : ",json_data['main']['temp_max'])
print("Description of ",city, "is : ",json_data['weather'][0]['description'])
