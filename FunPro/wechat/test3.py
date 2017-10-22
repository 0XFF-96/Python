import requests

apiUrl = 'https://www.tuling123.com/openapi/api'
data = {
	'key'	:'71f28bf79c820df10d39b4074345ef8c',# if this is't wroking ,
	'info'	:'hello', 
	'userid' : 'wechat-root' 

}

r = requests.post(apiUrl, data=data).json()

print(r)

