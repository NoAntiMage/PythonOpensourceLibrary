import requests

url = 'http://httpbin.org/post'

files = {'file': open('localfile.xls','rb')}
r = requests.post(url, files=files)
print(r.text)