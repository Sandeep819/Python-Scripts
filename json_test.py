import json

with open("json_files/medical.json") as f:
    data = json.load(f)

price = data['office']['medical'][2]

print(price)
print(type(price))
