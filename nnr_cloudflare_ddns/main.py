import requests
import settings

# nnr 请求头
nnr_headers = {"content-type": "application/json",
               "token": settings.nnr_api_token}

# 通过 api 请求 nnr 服务器列表
response = requests.post(url=settings.nnr_url, headers=nnr_headers)
data = response.json()

# 将 json 转为 python 对象
data = data["data"]

# 选取 name 为 target_name 的服务器
target = [server for server in data if server["name"] == settings.target_name]

# 选取 host ip
target = target[0]["host"]

# 创建新列表分割服务器 ip
target = target.split(",")

# 判断服务器 ip 数量
ip_num = len(target)
print(ip_num)