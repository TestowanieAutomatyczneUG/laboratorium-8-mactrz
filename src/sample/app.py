import requests

class Food:
    def getByName(self, name):
        r = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?', {'s': name})
        print(r.json())


food = Food()
food.getByName('Arrabiata')