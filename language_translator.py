import requests
print("###############LANGUAGE TRANSLATOR##########")
print("Available Language codes are according to ISO 9 lang codes. Example English: es, Spanish: es etc\n")
source_langauge = input("\nEnter source language\n")
target_langauge = input("\nEnter target language\n")
input_text = input("\nEnter input text to translate\n")

url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate?source="+source_langauge+"&target="+target_langauge+"&input="+input_text
headers={
    "X-RapidAPI-Host": "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "c1552a1e6cmsh6d968b2e7121932p1b4537jsn97529ffae3bc"
  }

json_data = requests.get(url,headers = headers ).json()


print("\nTraslated Data -> from "+source_langauge+" to "+target_langauge+" is ----->"+json_data['outputs'][0]['output'])
