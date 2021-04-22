from requests import Session
from bs4 import BeautifulSoup as bs
import re
from time import sleep

targetUsername = 'aviiiii_07'
targetUserid = '47370280198'

# Add fake accounts here
user_accs = {
"anexample12":"andthename",
"anexample101":"andthename",
"anexample1089":"yournameis",
"anexample3331":"ruthere",
"imdone107":"ruthat",
"everything45668":"everythinggood"
}
user_ids = ["47529367828","47569187561","47402419411","47554422088","47382181341","47251904696"]
#---------------
count = 0
for fake_username, fake_password in user_accs.items():
	fake_userid = user_ids[count]
	count+=1
	print()
	print("Account :", fake_username)
	with Session() as s:
		site = s.get("https://begeni.vip/girisyap")
		bs_content = str(bs(site.content, "html.parser"))
		token = re.search('antiForgeryToken=(.*)', bs_content)
		token = str(token.group(1).removesuffix('";'))
		payload = { 'username':fake_username,
			'password':fake_password,
			'userid':fake_userid,
			'antiForgeryToken':token}
		response = s.post("https://begeni.vip/girisyap", data=payload)
		print()
		response = str(response.content)
		print(response)
		if "success" not in response:
			continue
		print()
		print()
		payload = { 'adet':'10',
			'userID':targetUserid,
			'userName':targetUsername}
		response = s.post(f"https://begeni.vip/tools/send-follower/{targetUserid}?formType=send", data=payload)
		sleep(6)
		response = s.post(f"https://begeni.vip/tools/send-follower/{targetUserid}?formType=send", data=payload)
		sleep(6)
		if response.status_code == 200:
			print("Followers sent successful!")
		else:
			print("something went wrong, try again...")
