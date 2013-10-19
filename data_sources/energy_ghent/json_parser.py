import json
from pprint import pprint
json_data=open('energy2011.json')

data = json.load(json_data)
print (data)
