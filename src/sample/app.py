import requests

class Food:
    def getByName(self, name):
        r = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?', {'s': name})
        return r.json()['meals']
    def getById(self, id):
        return

food = Food()

print(food.getByName('Arrabiata'))