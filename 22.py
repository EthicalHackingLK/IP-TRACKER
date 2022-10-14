import requests
import pprint

B   = '\033[30m'
R     = '\033[31m'
G   = '\033[32m'
Y  = '\033[33m'
B    = '\033[34m'
M = '\033[35m'
C    = '\033[36m'
W   = '\033[37m'
E   = '\033[39m'

ip = requests.get('https://www.wikipedia.org').headers['X-Client-IP']
url = f"https://ipapi.co/{ip}/json/"
r = requests.get(url)
p=r.json()
print(B+"\nIP Address \033[39m = "+G,p['ip'])
print(B+"\nNetwork \033[39m = "+G,p['network'])
print(B+"\nIp Version \033[39m = "+G,p['version'])
print(B+"\nORG \033[39m = "+G,p['org'])
print(B+"\nCountry Name \033[39m = "+G,p['country_name'])
print(B+"\nCapital City \033[39m = "+G,p['country_capital'])
print(B+"\nCountry Area \033[39m = "+G,p['country_area'],'km²')
print(B+"\nCountry Population \033[39m = "+G,p['country_population'])
print(B+"\nCountry Code \033[39m = "+G,p['country_code'])
print(B+"\nCountry iso3 Code \033[39m = "+G,p['country_code_iso3'])
print(B+"\nCountry Calling Code \033[39m = "+G,p['country_calling_code'])
print(B+"\nCurrency \033[39m = "+G,p['currency'])
print(B+"\nCurrency Name \033[39m = "+G,p['country_name'],p['currency_name'])
print(B+"\nLanguages of The Country \033[39m = "+G,p['languages'])
print(B+"\nTime Zone \033[39m = "+G,p['timezone'])
print(B+"\nUTC Offset \033[39m = "+G,p['utc_offset'])
print(B+"\nCity of The User \033[39m = "+G,p['city'])
print(B+"\nLatitude \033[39m = "+G,p['latitude'])
print(B+"\nLongitude \033[39m = "+G,p['longitude'])
print(B+"\nRegion \033[39m = "+G,p['region'])
print(B+"\nRegion Code \033[39m = "+G,p['region_code'])

