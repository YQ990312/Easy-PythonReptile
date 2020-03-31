import requests
import json
response=requests.get("http://www.baidu.com")
print(response)
response.encoding="UTF-8"
requests_text=response.textS
print(requests_text)