# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

cities_dict = {
    "BY": ["Minsk", "Brest", "Pinsk"],
    "RU": ["Moscow", "Saint-Petersburg", "Kazan"],
    "LT": ["Vilnius", "Palanga", "Kaunas"],
    "US": ["New-York", "Washington", "Dallas"]
}

def country_search(target_city):
    for country, cities in cities_dict.items():
        if target_city in cities:
            return f"Belongs to: {country}"
    else:
        return "No country was found"

print(country_search(input("Enter city: ")))

