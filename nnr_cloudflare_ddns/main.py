
import requests
import settings

# NNR 请求头
nnr_headers = {"content-type": "application/json",
               "token": settings.nnr_api_token}

response = requests.post(url=settings.nnr_url, headers=nnr_headers)
data = response.json()
