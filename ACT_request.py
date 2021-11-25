import requests

ACT_req=requests.get('https://10.255.80.121/command-api',verify=False)
print(ACT_req)
print(ACT_req.content)
print(ACT_req.json) 