from requests import Session
from bs4 import BeautifulSoup as bs
import re
from time import sleep
import random
from datetime import datetime
import json
import string
import threading
from os import system
system('clear')

o = input("send to Avi ? ").lower()
if o=="" or o=="y" or o=="yes":
	targetUsername = 'aviiiii_07'
	targetUserid = '47370280198'
else:
	targetUsername = input("username : ")
	targetUserid = input("userid : ")

# Add fake accounts here

user_accs = {
"adi_tyaraj901": "",
"amanraj13442": "",
"ayush_panday4444": "",
"manav_ujjain": "",
"anshumanraj909": "",
"anshumankumar909": "",
"yamol30750": "",
"sanmanrak": "",
"pamexi1197": "",
"user556570": "",
"derof21844": "",
"ramkovind7099": "",
"heerasingh7099": "",
"anaman_chouchan": "",

}

#---------------

for key in user_accs:
	with open(key, 'r') as f:
		password = f.read().replace('\n','')
		user_accs[key] = password

def generate_password(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'
print("\n")
message = f"sending followers to {targetUsername}..."
go = True

def start_anim():
	while True:
		for yu in range(len(message)):
			if go == False:
				return
			list_str = list(message)
			list_str[yu] = list_str[yu].upper()
			print("\r"+"".join(list_str), end="")
			sleep(0.1)
           

anim = threading.Thread(target=start_anim)
anim.start()

def print_result():
	global go
	if go == True:
		go = False
		anim.join()
		print("\n\n")
		
def initiate_script(fake_username, fake_password):
	x = str(random.randint(100, 999))
	y = str(random.randint(10, 99))
	brands = ['xiaomi', 'vivo', 'samsung', 'micromax', 'oppo']
	user_agent = f"Mozilla/5.0 (Linux; Android {str(random.randint(9, 11))}; {random.choice(brands)} {str(random.randint(1000, 9999))}) AppleWebKit/{x}.{y} (KHTML, like Gecko) Chrome/{str(random.randint(10, 99))}.0.{str(random.randint(1000, 9999))}.{str(random.randint(100, 999))} Mobile Safari/{x}.{y}"
	with Session() as r:
		r.headers= {"user-agent":user_agent}
		r.headers.update({"Referer":link})
		response = r.get(link)
		csrf = re.findall(r"csrf_token\":\"(.*?)\"",response.text)[0]
		time = int(datetime.now().timestamp())
		payload = { 'username': fake_username, 'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{fake_password}', 'queryParams': {}, 'optIntoOneTap': 'false' }
		insta_response = r.post (login_url, data=payload, headers={ "User-Agent": user_agent, "X-Requested-With": "XMLHttpRequest", "Referer": "https://www.instagram.com/accounts/login/", "x-csrftoken": csrf })
		try:
			fake_userid = json.loads(insta_response.text)['userId']
		except:
			print_result()
			print("\nAccount : " + fake_username + f"\033[91m - Error\033[0m\n{insta_response.text}\n")
			r.close()
			return False
		with Session() as s:
			site = s.get("https://begeni.vip/girisyap")
			bs_content = str(bs(site.content, "html.parser"))
			token = re.search('antiForgeryToken=(.*)', bs_content)
			token = str(token.group(1).removesuffix('";'))
			payload = { 'username':fake_username,'password':fake_password,'userid':fake_userid,'antiForgeryToken':token}
			f_response = s.post("https://begeni.vip/girisyap", data=payload)
			if "success" not in f_response.text:
				print_result()
				print("\nAccount : " + fake_username + f"\033[91m - Error\033[0m\n{insta_response.text}\n{f_response.text}\n")
				r.close()
				s.close()
				return False
			new_pass = generate_password(10)
			sleep_time = random.randint(6,12)
			payload = { 'adet':'10','userID':targetUserid,'userName':targetUsername}
			response = s.post(f"https://begeni.vip/tools/send-follower/{targetUserid}?formType=send", data=payload)
			sleep(sleep_time)
			response = s.post(f"https://begeni.vip/tools/send-follower/{targetUserid}?formType=send", data=payload)
			sleep(sleep_time)
			response = s.post(f"https://begeni.vip/tools/send-follower/{targetUserid}?formType=send", data=payload)
			sleep(sleep_time)
			response = s.post(f"https://begeni.vip/tools/send-follower/{targetUserid}?formType=send", data=payload)
			sleep(sleep_time)
			s.close()
		# Now change password
		e = r.get(f"https://www.instagram.com/{fake_username}/")
		time = int (datetime.now ().timestamp ())
		payload = { 'enc_old_password':f'#PWD_INSTAGRAM_BROWSER:0:{time}:{fake_password}',
		'enc_new_password1':f'#PWD_INSTAGRAM_BROWSER:0:{time}:{new_pass}',
		'enc_new_password2':f'#PWD_INSTAGRAM_BROWSER:0:{time}:{new_pass}'
		}
	
		headers = {
			"Host": "www.instagram.com",
			"User-Agent": user_agent,
			"Accept": "*/*",
			"Accept-Language": "en-US,en;q=0.5",
			"Accept-Encoding": "gzip, deflate, br",
			"Referer": "https://www.instagram.com/accounts/password/change/",
			"X-CSRFToken": e.cookies['csrftoken'],
			"X-Requested-With": "XMLHttpRequest",
			"DNT": "1",
			"TE": "Trailers",
			"Connection": "keep-alive",
			"Cookie": e.request.headers['cookie']
				}
		pass_response = r.post("https://www.instagram.com/accounts/password/change/", headers = headers, data = payload)
		if 'ok' in pass_response.text:
			print_result()
			print("Account : " + fake_username + "\033[92m - OK\033[0m")
			with open(fake_username, 'w+') as f:
				f.write(new_pass)
		else:
			print_result()
			print("\nAccount : " + fake_username + f"\033[91m - Error\033[0m\n{insta_response.text}\n{f_response.text}\n{pass_response.txt}\n")
		r.close()
		
for fake_username, fake_password in user_accs.items():
	sleep(random.randint(1,3))
	sc = threading.Thread(target=initiate_script, args=[fake_username, fake_password])
	sc.start()
