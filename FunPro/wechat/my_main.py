
import requests

import itchat

KEY = ''

def get_response(msg):

	apiUrl = ''

	data = {

		'key'	:key,
		'info'	:msg,
		'userid' : 'wechat-root',
	}

	try :

		r = requests.post(apiUrl, data=data).json()

		return r.get('text')

	except:

		return 

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):

	defaultReply = 'I received : ' + msg['Text']
	
	reply = get_response(msg['Text'])

	return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
	
