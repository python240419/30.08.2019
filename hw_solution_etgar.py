import requests
import json


class User:
    def __init__(self, d):
        self.__dict__ = d
        self.address = Address(self.address)

    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += f'{k} - {v}\n'
        return result


class Address:
    def __init__(self, d):
        self.__dict__ = d

    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += f'{k} - {v}\n'
        return result


def getUsers():
    resp = requests.get('http://jsonplaceholder.typicode.com/users')
    return json.loads(resp.content)  # Users List


def findUser(nameToCheck, userList):
    for user in userList:
        check = User(user)
        if check.name == nameToCheck:
            return check


userJson = getUsers()
a = findUser('Glenna Reichert', userJson)

print(a.address.city)
