import requests
import json
'''百度翻译有一个反爬的工作，用一个'sign一个来判断每一个的翻译单词，每个词的sign不一样''
Chinese=input("输入中文")
request_data={"query": "你好世界",
              "from": "zh",
              "to": "en",  
              "token": "6e07dea5d18bfd0565c1015c8203e97e",
              "sign": "585444.789973"            
              }
request_headers={"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
                 "referer": "https://fanyi.baidu.com/",
                 "cookie":"BAIDUID=A9856A500C88D4F20D4495FB29DCA8E1:FG=1; PSTM=1568214749; BIDUPSID=A9856A500C88D4F20D4495FB29DCA8E1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; H_PS_PSSID=1420_21103_30211; delPer=0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1576070261,1576496946,1576497030,1576498621; __yjsv5_shitong=1.0_7_96e81560d53f44e66b8ab82cfb22f2712799_300_1576498621814_59.52.109.207_e49f7887; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1576500603; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1576500603; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1576500603; yjs_js_security_passport=f3b35e416b0513ff626674f31230ab4bd24443ac_1576500606_js"}
response=requests.post("https://fanyi.baidu.com/basetrans",data=request_data,headers=request_headers)
print(type(response))
print(response.content.decode())
response_dirt=json.loads(response.content.decode())
print(response_dirt["trans"][0]["dst"])