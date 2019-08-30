import requests
import json

class Photo:
    def __init__(self, d):
        self.__dict__ = d
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result

number = int(input("Enter a photot number: "))
resp = requests.get(f'http://jsonplaceholder.typicode.com/photos/{number}')
resp_dict = json.loads(resp.content)
#if (len(resp_dict.items()) == 0):
if (resp.status_code == 404):
    print(f'Photo #{number} Does not exist')
else:
    photo = Photo(resp_dict)
    print(photo)

