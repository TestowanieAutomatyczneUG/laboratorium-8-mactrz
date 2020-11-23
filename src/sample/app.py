import requests

class Food:
    def getByName(self, name):
        if type(name) != str:
            raise Exception('Name must be a string!')
        r = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?', {'s': name})
        return r.json()['meals']

    def getById(self, id):
        if type(id) != int:
            raise Exception('Id must be an integer!')
        r = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?', {'i': str(id)})
        return r.json()['meals']

    def listByLetter(self, letter):
        r = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?', {'f': letter})
        return r.json()['meals']

food = Food()

print(food.getByName('Arrabiata'))
print(food.listByLetter('z'))