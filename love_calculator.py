import requests

fname = input("\nEnter first name\n")
sname = input("\nEnter second name\n")


url  = "https://love-calculator.p.rapidapi.com/getPercentage?fname="+fname+"&sname="+sname
headers={
    "X-RapidAPI-Host": "love-calculator.p.rapidapi.com",
    "X-RapidAPI-Key": "c1552a1e6cmsh6d968b2e7121932p1b4537jsn97529ffae3bc"
  }

json_data = requests.get(url,headers=headers).json()

print(json_data)

print("\n\n##### Love Calculator ########\n\n")
print("\nHere is success percentage : "+json_data['percentage']+"%\n")
print("\nSuggestion : "+json_data['result']+"\n")



