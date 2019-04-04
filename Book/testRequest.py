import requests
import json

# 接口的url
# url = "http://fanyi.baidu.com/v2transapi"
url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
# 接口的参数
params = {
    "from":"en",
    "to":"zh",
    "query": "test"
}

# 发送接口
r = requests.request("post", url, params=params)

# 打印返回结果
print(r.text)


# d = json.loads(r.text)
# print(d['liju_result']['tag'])
# 返回结果