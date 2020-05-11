import requests
import json
url = 'http://127.0.0.1:5000/'
data = {
    'IP': '123456',
    'Aadhar': '1',
    'Vote': '2'

}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

result = requests.post(url=url, data=json.dumps(data), headers=headers)
print(result)