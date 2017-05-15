import json
import requests

accessToken = "" #put your access token between the quotes.


accessToken_hdr = 'Bearer ' + MWU1ZDE4YzItMjllMi00YjdiLWExYzktZDNkODFlZDk4N2FjOTJmNjI4MTQtZWZl
spark_header = {'Authorization': accessToken_hdr}
uri = 'https://api.ciscospark.com/v1/rooms'
resp = requests.get(uri, headers=spark_header)
print("Spark Rooms you belong to: ")	
print(resp.text)

print()
print("Spark Rooms in easier to read format - pretty format:")
print (json.dumps(resp.json(), indent=4, separators=(',', ': ')))

