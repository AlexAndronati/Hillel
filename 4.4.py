
def auto_key(autos_dict: dict):
    if autos_dict.get("price") is not None:
        return autos_dict.get("price")
    else:
        return 0


autos = [
   {"brand": "Ford", "model": "Mustang", "year": 1964, 'price': 4000},
   {"brand": "Ford", "model": "Mondeo", "year": 1999, 'price': 3000},
   {"brand": "Ford", "model": "Fiesta", "year": 2003, 'price': 4200},
   {"brand": "Nissan", "model": "Primera", "year": 1997, 'price': 3100},
   {"brand": "BMW", "model": "X3", "year": 2001, 'price': 5000},
   {"brand": "Nissan", "model": None, "year": 1964, 'price': None},
   {"brand": "VW", "model": "Passat", "year": 1996, 'price': 1200},
   {"brand": "BMW", "model": "X5", "year": 2010, 'price': 7500},
   {"brand": "Renault", "model": "Megane", "year": 1999, 'price': 2300},
]

print(*sorted(autos, key=auto_key, reverse=True), sep="\n")
print("\n\n")
print(*sorted(autos, key=lambda autos_dict: autos_dict.get("price") or 0, reverse=True), sep="\n")
