import requests


api_address = "http://api.openweathermap.org/data/2.5/weather?appid=8c3aad91151f7346f0719bda6082aba5&q="

print("\nThis script generates report based on the entered city \n")

city = input("Enter a city name : ")

url = api_address + city

json_data = requests.get(url).json()


if(json_data['cod'] == '404'):
  print("\nOOPS !! City not found\n")
elif(json_data['cod'] == '400'):
  print("\nPlease enter any city name\n")
else:
  print("\n\n#####Weather Report########\n\n")
  print("Temparature now in ",city, "is : ",json_data['main']['temp']-273.15,"C")
  print("Pressure now in ",city, "is : ",json_data['main']['pressure'],"hPa")
  print("Humidity now in ",city, "is : ",json_data['main']['humidity'],"%")
  print("Minimum Temparature now in ",city, "is : ",json_data['main']['temp_min']-273.15,"C")
  print("Maximum Temparature now in ",city, "is : ",json_data['main']['temp_max']-273.15,"C")
  print("Description of ",city, "is : ",json_data['weather'][0]['description'])
