import requests
url="https://item.jd.com/3505232.html"
response=requests.get(url)
print(response.content.decode("gbk"))
# with open("yjq.html","w",encoding="utf-8") as f:
#     f.write(response.content.decode())