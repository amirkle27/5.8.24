country_dict: dict = {"name": "Israel", "birth": 1948, "population_millions": 9.3, "capital": "Jerusalem", "language": "Hebrew", "cities": ["Jerusalem", "Tel Aviv", "Haife", "Rishon LeZion", "Petah Tikva", "Ashdod"],"currency": "ILS", "area_kilometer": 22145, "gdp_billion": 450}

#a#

print(country_dict.get("capital"))

#b#

print(country_dict.keys())

#c#

#keys_list = [country_dict.keys()]
#print(str(keys_list).upper())

print(list(str(keys_list).upper() for keys_list in (country_dict.keys())))

#d#

print(country_dict.values())

#e#

print("Values length:", list(map(lambda values: len(str(values)), country_dict.values())))

#f#

print(country_dict.items())

#g#

copied_country_dict = country_dict.copy()
print(f"copied_country_dict: {copied_country_dict}")

#h#

copied_country_dict.clear()
print(f"copied_country_dict: {copied_country_dict}")

#i#

new_dict: dict = country_dict.fromkeys(country_dict)
print(f"new_dict: {new_dict}")

#j#

del new_dict ["currency"]
print(new_dict)

#k#

new_dict.pop("area_kilometer")
print(new_dict)

#l(i),(ii)#

new_dict.update({"national_sprt": "Soccer", "population_millions": 9.4})
print(new_dict)
