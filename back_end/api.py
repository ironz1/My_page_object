import requests
res = requests.get(url='https://wp.pl')
print(res.status_code)
print(res.headers)
print(res.text)