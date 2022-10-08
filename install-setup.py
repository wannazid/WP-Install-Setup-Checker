# mass check wp install & wp setup config by wannazid
import requests
import random
import argparse
from concurrent.futures import ThreadPoolExecutor

red = "\033[31;1m"
green = "\033[32;1m"
yellow = "\033[33;1m"
white = "\033[37;1m"

parser = argparse.ArgumentParser(description='[!] Mass Check WP Setup Config & WP Install ')
parser.add_argument('-l', '--list', metavar='', type=str, help='List Site or List Site Target')
parser.add_argument('-t', '--thread', metavar='', type=int, help='Thread Tools')
args = parser.parse_args()
	
class Main:
	def __init__(self, domain):
		self.domain = domain
		self.wp_setup()
		self.wp_install()
	
	def user_agent(self):
		ua = open('user-agents.txt', 'r').read().splitlines()
		return random.choice(ua)
	
	def wp_setup(self):
		try:
			for y in " ":
				Agent = {'User-Agent':self.user_agent()}
				exploit = self.domain+ '/wp-admin/setup-config.php?step=1'
				req = requests.get(exploit, headers=Agent)
				if '<form method="post" action="setup-config.php?step=2">' in req.text:
					print(f'{green}[#] {exploit} > Exist')
					open('Exist Setup Config.txt','a').write(exploit+'\n')
				else:
					print(f'{red}[#] {exploit} > Not Exist')
					open('Not Exist Setup Config.txt','a').write(exploit+'\n')
		except Exception as e:
			print(f'{yellow}[!] {exploit} : {e}')
			
	def wp_install(self):
		try:
			for x in " ":
				Agents = {'User-Agent':self.user_agent()}
				exploit1 = self.domain+'/wp-admin/install.php?step=1'
				r = requests.get(exploit1, headers=Agents)
				if '<form id="setup" method="post" action="install.php?step=2" novalidate="novalidate">' in r.text:
					print(f'{green}[#] {exploit1} > Exist')
					open('Exist WP Install.txt','a').write(exploit1+'\n')
				else:
					print(f'{red}[#] {exploit1} > Not Exist')
					open('Not Exist WP Install.txt','a').write(exploit1+'\n')
		except Exception as e:
			print(f'{yellow}[!] {exploit1} : {e}')
			
if __name__ == '__main__':
	banner = f'''{white}
            /(`o
      ,-,  //  \\
     (,,,) ||   V
    (,,,,)\//
    (,,,/w)-'
    \,,/w)    | Mass Check WP Setup Config & WP Install |
    `V/uu            ~ by : wannazid
      / |            ~ github : github.com/wannazid
      | |
      o o
      \ |
 \,/  ,\|,.  \,/
	'''
	print(banner)
	
	try:
		open_site = open(args.list,'r').read().splitlines()
		duplicates = set(open_site)
		site = list(duplicates)
		with ThreadPoolExecutor(max_workers=int(args.thread)) as t:
			[t.submit(Main, dom) for dom in site]
	except Exception as e:
			print(f' {yellow}Error : {e}{white}\n\n [!] Usage : python3 install-setup.py -l list.txt -t thread\n [!] Help : python3 install-setup.py -h\n')
			