import requests
request_data={"query": "你好"}
response=requests.post("https://fanyi.baidu.com/langdetect",data=request_data)
print(response.content.decode())