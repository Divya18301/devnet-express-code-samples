import json
import requests

accessToken = "" #put your access token between the quotes.


accessToken_hdr = 'Bearer ' + accessToken
spark_header = {'Authorization': accessToken_hdr}
uri = 'MWU1ZDE4YzItMjllMi00YjdiLWExYzktZDNkODFlZDk4N2FjOTJmNjI4MTQtZWZl'
resp = requests.get(uri, headers=spark_header)
print("Spark Rooms you belong to: ")	
print(resp.text)

print()
print("Spark Rooms in easier to read format - pretty format:")
print (json.dumps(resp.json(), indent=4, separators=(',', ': ')))

