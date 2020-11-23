import requests

class Food:
    def getByName(self, name):
        r = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?', {'s': name})
        return r.json()['meals'][0]

    def getById(self, id):
        r = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?', {'i': id})
        return r.json()['meals'][0]

food = Food()

print(food.getByName('Arrabiata'))
print(food.getById('52772'))