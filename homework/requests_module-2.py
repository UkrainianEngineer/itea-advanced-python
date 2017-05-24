# pip install requests

import requests

r = requests.get('https://openweathermap.org')

print r.status_code
print r.headers['content-type']
print r.encoding
r.encoding = 'ISO-8859-1'
print r.encoding
# print r.text # show code page

# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# r = requests.put('http://httpbin.org/put', data = {'key':'value'})
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://openweathermap.org', params=payload)
print(r.url)

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://openweathermap.org/get', params=payload)
print(r.url)

# print r.content
# from PIL import Image
# from io import BytesIO
# i = Image.open(BytesIO(r.content))
# print i
# with open('requests_file.json', 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)
url = 'https://openweathermap.org/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print r