# pip install requests

import requests

r = requests.get('https://api.github.com/events')
print(type(r))
print(r.__doc__)

# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)

payload = {'key1': 'value1', 'key2[]': ['value2', 'value3']}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)

r = requests.get('https://api.github.com/events')
# print(r.text)

r = requests.get('https://api.github.com/events', stream=True)
print(r.raw)
print(r.raw.read(10))


