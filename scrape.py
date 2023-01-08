import random
import requests
from bs4 import BeautifulSoup
import sys,time,os
from colorama import *
message = """
  ___          _ _ _        _      ___  _    _                      _   ___         _ _         ___                            
 | _ \___ __ _| (_) |_ _  _( )___ |   \(_)__| |__  ___  __ _ _ _ __| | |_ _|_ ___ _(_) |_ ___  / __| __ _ _ __ _ _ __  ___ _ _ 
 |   / -_) _` | | |  _| || |/(_-< | |) | (_-< '_ \/ _ \/ _` | '_/ _` |  | || ' \ V / |  _/ -_) \__ \/ _| '_/ _` | '_ \/ -_) '_|
 |_|_\___\__,_|_|_|\__|\_, | /__/ |___/|_/__/_.__/\___/\__,_|_| \__,_| |___|_||_\_/|_|\__\___| |___/\__|_| \__,_| .__/\___|_|  
                       |__/                                                                                     |_|            
"""
print(Fore.GREEN + message)
print(Style.RESET_ALL)
tag = input("What tag do you want to scrape invites from? : ")
print(Style.RESET_ALL)
URL = "https://disboard.org/servers/tag/" + tag
URL2 = "https://disboard.org/servers/tag/" + tag + "/2"
URL3 = "https://disboard.org/servers/tag/" + tag + "/3"
URL4 = "https://disboard.org/servers/tag/" + tag + "/4"
URL5 = "https://disboard.org/servers/tag/" + tag + "/5"
URL6 = "https://disboard.org/servers/tag/" + tag + "/6"
URL7 = "https://disboard.org/servers/tag/" + tag + "/7"
URL8 = "https://disboard.org/servers/tag/" + tag + "/8"
URL9 = "https://disboard.org/servers/tag/" + tag + "/9"
URL10 = "https://disboard.org/servers/tag/" + tag + "/10"
URL11 = "https://disboard.org/servers/tag/" + tag + "/11"
URL12 = "https://disboard.org/servers/tag/" + tag + "/12"
URL13 = "https://disboard.org/servers/tag/" + tag + "/13"
URL14 = "https://disboard.org/servers/tag/" + tag + "/14"
URL15 = "https://disboard.org/servers/tag/" + tag + "/15"
URL16 = "https://disboard.org/servers/tag/" + tag + "/16"
URL17 = "https://disboard.org/servers/tag/" + tag + "/17"
URL18 = "https://disboard.org/servers/tag/" + tag + "/18"
URL19 = "https://disboard.org/servers/tag/" + tag + "/19"
URL20 = "https://disboard.org/servers/tag/" + tag + "/20"
URL21 = "https://disboard.org/servers/tag/" + tag + "/21"
print("Scraping.")
usr_agents = [ 
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
"Links (2.1pre15; FreeBSD 5.4-STABLE i386; 158x58)",
"Wget/1.8.2",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.0",
"Mediapartners-Google/2.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.5) Gecko/20031007 Firebird/0.7",
"Mozilla/4.04 [en] (WinNT; I)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20060205 Galeon/2.0.0 (Debian package 2.0.0-2)",
"lwp-trivial/1.41",
"Dillo/0.8.5-i18n-misc",
"NetBSD-ftp/20031210",
"Wget/1.10.2",
"Links (2.1pre20; NetBSD 2.1_STABLE i386; 145x54)",
"Lynx/2.8.5rel.5 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d",
"Lynx/2.8.5rel.3 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d",
"Links (2.1pre19; NetBSD 2.1_STABLE sparc64; 145x54)",
"Lynx/2.8.6dev.15 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d",
"Links (2.1pre14; IRIX64 6.5 IP27; 145x54)",
"Wget/1.10.1",
"ELinks/0.10.5 (textmode; FreeBSD 4.11-STABLE i386; 80x22-2)",
"Links (2.1pre20; FreeBSD 4.11-STABLE i386; 80x22)",
"Lynx/2.8.5rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d-p1",
"Opera/8.52 (X11; Linux i386; U; de)",
"Mozilla/5.0 (X11; U; NetBSD i386; en-US; rv:1.8.0.1) Gecko/20060310 Firefox/1.5.0.1",
"Mozilla/5.0 (X11; U; IRIX64 IP27; en-US; rv:1.4) Gecko/20030711",
"Mozilla/4.8 [en] (X11; U; IRIX64 6.5 IP27)",
"Mozilla/4.76 [en] (X11; U; SunOS 5.8 sun4m)",
"Opera/5.0 (SunOS 5.8 sun4m; U) [en]",
"Links (2.1pre15; SunOS 5.8 sun4m; 80x24)",
"Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d",
"Wget/1.8.1",
"Wget/1.9.1",
"tnftp/20050625",
"Links (1.00pre12; Linux 2.6.14.2.20051115 i686; 80x24) (Debian pkg 0.99+1.00pre12-1)",
"Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.0.16",
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.7) Gecko/20051122",
"Wget/1.7",
"Lynx/2.8.2rel.1 libwww-FM/2.14",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; de) Opera 8.53",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; de; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1",
"Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7e",
"Links (2.1pre20; SunOS 5.10 sun4u; 80x22)",
"Lynx/2.8.5rel.5 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7i",
"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8) Gecko/20060202 Firefox/1.5",
"Opera/8.51 (X11; Linux i386; U; de)",
"Emacs-W3/4.0pre.46 URL/p4.0pre.46 (i386--freebsd; X11)",
"Links (0.96; OpenBSD 3.0 sparc)",
"Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.6c",
"Lynx/2.8.3rel.1 libwww-FM/2.14",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
"libwww-perl/5.79",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.53",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.12) Gecko/20050919 Firefox/1.0.7",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)",
"msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
"Googlebot/2.1 (+http://www.google.com/bot.html)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051008 Firefox/1.0.7",
"Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.51",
"Mozilla/5.0 (compatible; Konqueror/3.4; Linux) KHTML/3.4.3 (like Gecko)",
"Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7c",
"Mozilla/4.0 (compatible; MSIE 6.0; AOL 9.0; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/4.8 [en] (Windows NT 5.1; U)",
"Opera/8.51 (Windows NT 5.1; U; en)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
"Opera/8.51 (Windows NT 5.1; U; en;VWP-online.de)",
"sproose/0.1-alpha (sproose crawler; http://www.sproose.com/bot.html; crawler@sproose.com)",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.1) Gecko/20060130 SeaMonkey/1.0",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.1) Gecko/20060130 SeaMonkey/1.0,gzip(gfe) (via translate.google.com)",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1",
"BrowserEmulator/0.9 see http://dejavu.org",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:0.9.4.1) Gecko/20020508",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.2 (KHTML, like Gecko)",
"Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.4) Gecko/20030624",
"iCCrawler (http://www.iccenter.net/bot.htm)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.6) Gecko/20050321 Firefox/1.0.2",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; Maxthon; .NET CLR 1.1.4322)",
"Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.7.12) Gecko/20051013 Debian/1.7.12-1ubuntu1",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de; rv:1.8) Gecko/20051111 Firefox/1.5",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322)",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; de) Opera 8.50",
"Mozilla/3.0 (x86 [de] Windows NT 5.0; Sun)",
"Java/1.4.1_04",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8) Gecko/20051111 Firefox/1.5",
"msnbot/0.9 (+http://search.msn.com/msnbot.htm)",
"NutchCVS/0.8-dev (Nutch running at UW; http://www.nutch.org/docs/en/bot.html; sycrawl@cs.washington.edu)",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.53",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.4) Gecko/20030619 Netscape/7.1 (ax)",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.6",
"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt)",
"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 4.0)",
"Mozilla/4.0 (compatible; MSIE 5.16; Mac_PowerPC)",
"Mozilla/4.0 (compatible; MSIE 5.01; Windows 98)",
"Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt)",
"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)",
"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 5.0; Windows 95)",
"Mozilla/4.0 (compatible; MSIE 5.5; AOL 7.0; Windows 98)",
"Mozilla/4.0 (compatible; MSIE 5.17; Mac_PowerPC)",
"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)",
"Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC)",
"Opera/8.53 (Windows NT 5.1; U; en)"
]
print("Scraping..")
random_user_agent = random.choice(usr_agents)
headers = {
    'User-Agent': random_user_agent
}
response = requests.get(URL, headers=headers)
response2 = requests.get(URL2, headers=headers)
response3 = requests.get(URL3, headers=headers)
response4 = requests.get(URL4, headers=headers)
response5 = requests.get(URL5, headers=headers)
response6 = requests.get(URL6, headers=headers)
response7 = requests.get(URL7, headers=headers)
response8 = requests.get(URL8, headers=headers)
response9 = requests.get(URL9, headers=headers)
response10 = requests.get(URL10, headers=headers)
response11 = requests.get(URL11, headers=headers)
response12 = requests.get(URL12, headers=headers)
response13 = requests.get(URL13, headers=headers)
response14 = requests.get(URL14, headers=headers)
response15 = requests.get(URL15, headers=headers)
response16 = requests.get(URL16, headers=headers)
response17 = requests.get(URL17, headers=headers)
response18 = requests.get(URL18, headers=headers)
response19 = requests.get(URL19, headers=headers)
response20 = requests.get(URL20, headers=headers)
response21 = requests.get(URL21, headers=headers)

print("Scraping...")
soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')
soup3 = BeautifulSoup(response3.text, 'html.parser')
soup4 = BeautifulSoup(response4.text, 'html.parser')
soup5 = BeautifulSoup(response5.text, 'html.parser')
soup6 = BeautifulSoup(response6.text, 'html.parser')
soup7 = BeautifulSoup(response7.text, 'html.parser')
soup8 = BeautifulSoup(response8.text, 'html.parser')
soup9 = BeautifulSoup(response9.text, 'html.parser')
soup10 = BeautifulSoup(response10.text, 'html.parser')
soup11 = BeautifulSoup(response11.text, 'html.parser')
soup12 = BeautifulSoup(response12.text, 'html.parser')
soup13 = BeautifulSoup(response13.text, 'html.parser')
soup14 = BeautifulSoup(response14.text, 'html.parser')
soup15 = BeautifulSoup(response15.text, 'html.parser')
soup16 = BeautifulSoup(response16.text, 'html.parser')
soup17 = BeautifulSoup(response17.text, 'html.parser')
soup18 = BeautifulSoup(response18.text, 'html.parser')
soup19 = BeautifulSoup(response19.text, 'html.parser')
soup20 = BeautifulSoup(response20.text, 'html.parser')
soup21 = BeautifulSoup(response21.text, 'html.parser')
print("Scraping....")

buttons = soup.find_all(class_='button button-join is-discord')
buttons2 = soup2.find_all(class_='button button-join is-discord')
buttons3 = soup3.find_all(class_='button button-join is-discord')
buttons4 = soup4.find_all(class_='button button-join is-discord')
buttons5 = soup5.find_all(class_='button button-join is-discord')
buttons6 = soup6.find_all(class_='button button-join is-discord')
buttons7 = soup7.find_all(class_='button button-join is-discord')
buttons8 = soup8.find_all(class_='button button-join is-discord')
buttons9 = soup9.find_all(class_='button button-join is-discord')
buttons10 = soup10.find_all(class_='button button-join is-discord')
buttons11 = soup11.find_all(class_='button button-join is-discord')
buttons12 = soup12.find_all(class_='button button-join is-discord')
buttons13 = soup13.find_all(class_='button button-join is-discord')
buttons14 = soup14.find_all(class_='button button-join is-discord')
buttons15 = soup15.find_all(class_='button button-join is-discord')
buttons16 = soup16.find_all(class_='button button-join is-discord')
buttons17 = soup17.find_all(class_='button button-join is-discord')
buttons18 = soup18.find_all(class_='button button-join is-discord')
buttons19 = soup19.find_all(class_='button button-join is-discord')
buttons20 = soup20.find_all(class_='button button-join is-discord')
buttons21 = soup21.find_all(class_='button button-join is-discord')
print("Scraping.......")
file = open('invites.txt', 'w')

for button in buttons:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons2:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons3:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons4:
    file.write("\nhttps://disboard.org" + button['href'])    
for button in buttons5:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons6:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons7:
    file.write("\nhttps://disboard.org" + button['href'])    
for button in buttons8:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons9:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons10:
    file.write("\nhttps://disboard.org" + button['href'])    
for button in buttons11:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons12:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons13:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons14:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons15:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons16:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons17:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons18:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons19:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons20:
    file.write("\nhttps://disboard.org" + button['href'])
for button in buttons21:
    file.write("\nhttps://disboard.org" + button['href'])
print("Succesfully Scraped & Wrote all of the Invites to invites.txt")
