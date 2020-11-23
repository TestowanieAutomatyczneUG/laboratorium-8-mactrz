import requests

class Food:
    def getByName(self, name):
        r = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?', {'s': name})
        return r.json()['meals']


food = Food()

print(food.getByName('Arrabiata'))