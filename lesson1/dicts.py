from pprint import pprint

weather = {"city": "Москва", "temperature": "20"}
print(weather.get("city"))

weather["temperature"] = str(int(weather["temperature"]) - 5)
pprint(weather)

print("country" in weather)
print(bool(weather.get("country")))
print(weather.get("country", "Россия"))

weather["date"] = "27.05.2019"

pprint(weather)
print(len(weather))

