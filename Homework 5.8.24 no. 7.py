countries = [{'name': 'Israel', 'population': 9.3, 'birth': 1948},
             {'name': 'United States', 'population': 331.9, 'birth': 1776},
             {'name': 'Japan', 'population': 125.8, 'birth': 660},
             {'name': 'Australia', 'population': 25.7, 'birth': 1901},
             {'name': 'Canada', 'population': 38.0, 'birth': 1867}]

print("Countries with more than 30m people:", list(filter(lambda country: country['population'] > 30, countries)))
print("Countries established after 1800:", list(filter(lambda country: country ['birth'] >1800, countries)))
print("Only names of countries:", list(map(lambda country: country ['name'], countries)))
print("Only establishment years:", list(map(lambda country: country ['birth'], countries)))
print("Countries sorted by Establishment dates:", sorted (countries, key = lambda country: country ['birth']))
print("Countries sorted by population:", sorted(countries, key= lambda country: country ['population']))