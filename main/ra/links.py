        #with open ('C:/Users/Valued Client/Desktop/html/springerBooks.html', 'r', errors='ignore') as html_file:
        #content = html_file.read()
        #print(content)
        #soup = BeautifulSoup(content, 'html.parser')
import bs4
from bs4 import BeautifulSoup
import os
import requests
import random
import time


#from fake_user_agent import UserAgent
        

def springer(word, proxy):
    
    
    #response = data_scraper('get', 'https://www.springeropen.com/search?query=' + word + '&searchType=publisherSearch', headers = headers())
    response = requests.get('https://www.springeropen.com/search?query=' + word + '&searchType=publisherSearch', headers = headers(), proxies={'https:': proxy}, timeout=5) #articles
    
    #response = requests.get('https://www.springer.com/gp/search?query=' + word + '&submit=Submit', headers = headers(), proxies={'https:': proxy}, timeout=5) #books
    #print(response.json())  
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())
    return soup


def proxy_generators():


    
    
   
    response = requests.get('https://free-proxy-list.net/', headers = headers())
    soup = BeautifulSoup(response.content, 'html.parser')
    
        
    page= soup.find('textarea', class_='form-control')
    a =page.text
    proxies = a[75:].split("\n")
    #print(proxies)

    return proxies

    #with open('C:/Users/Valued Client/Desktop/proxies.txt', 'w') as file:    / writing in a file /
    #with open ('C:/Users/Valued Client/Desktop/free proxy.html', 'r', errors='ignore') as html_file:   / opening a file /
            #content = html_file.read()
            #soup = BeautifulSoup(content, 'html.parser')
        #response = requests.get("https://free-proxy-list.net/")
        #soup = BeautifulSoup(response.content, 'html.parser')

        #print(a.readline())   / reading a line in the file/
        #rows = page.text
        
        #tr = page.findAll('tr')
        #rowCtr = 0
        
        #for row in tr:
            #columnCtr = 0
            #temp =[]
            #if rowCtr > 0 and rowCtr < 21:
                #for column in row:
                    #temp.append(column.text)
                    #columnCtr = columnCtr + 1

            #if len(temp) != 0:
                #if (temp[4] == 'elite proxy' and temp[6] == 'yes'):
                    #file.write('https://' + temp[0] + ':' + temp[1] + "\n")
            
            #rowCtr = rowCtr + 1


def practice():
    with open ('C:/Users/Valued Client/Desktop/html/springerBooks.html', 'r', errors='ignore') as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content, 'html.parser')

        rows = soup.find('div', id='result-list')

        

        for a in range(22):
            books1 = rows.find('div', class_='result-item result-item-' + str(a) + ' result-type-book')
            books2 = rows.find('div', class_='result-item result-item-' + str(a) + ' result-type-book last')
            editorial = rows.find('div', class_='result-item result-item-' + str(a) + ' result-type-editorial')

            if editorial != None:
                title =editorial.h4.text 
                print(editorial.h4.text)
            elif books1 != None:
                print(books1.h4.text)
                print(books1.div.text)
                print(books1.find('p', class_='format').text)
            elif books2 != None:
                print(books2.h4.text)
                

        
                
    
    
   


    
def scienceDirect(p):
    word = 'engineer'
    #ua = random.choice(userAgents) 
    headers = {
    'authority': 'www.sciencedirect.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://id.elsevier.com/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'EUID=75fdfe63-504d-4c8a-8180-c03a43da237c; utt=2146-84ee935a77144283645aebe835a645e74f7-M0M6; mboxes=%7B%22universal-view-pdf%22%3A%7B%22variation%22%3A%22B%22%7D%2C%22article-page-remote-access-button-location-server-side-mbox%22%3A%7B%22variation%22%3A%22D%22%7D%7D; mbox=session%23e7585ea25ab6444dae178e8f7680b6a8%231629353135%7CPC%2370b4195123dc401fa07762b437030b81.34_0%231692596075; fingerPrintToken=c5573f441dc477fbc29e95fc733bc9fc; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; __cf_bm=c1c4c417dc39687020a2e9d513f6d80db5e3c7b8-1629865070-1800-AZsz+wVIEksG+5D8sVd0uBZ6baBr1fA4nbpsl7TC3TbJfgN9Dh4IcIv0DAUA09YPmR/c5qdKYRi8cjHqWYqGcfBQwWOE1S87rtd33NrvRny2; acw=0e1c82089f7f754e317aac502e63709f9365gxrqa%7C%24%7CD67EEA336862179B96C7A4E612EEB3B7E0D22937694E131AFB2580493A393B3465EF33CC0CB6D0665D6E0481940F976214CA280CAC27B2BE5B2791389D9DC89EC6BBDAFCBBAE3D67F47FA9700FFD7D78; sd_access=eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..JDN24MHPbbNqf4SjLbIhGQ.y12rLDbzwqtn6QLt95NbuWUAr82FBGzrAB9VoRAE9uAI8otvvOX53fZ3AN7fv2vFbeLgmICwbdPK3L3PLkBN_QsDYocvDskDnmm7fTd69mi6fZbyBMI80TCLZsrGca_IItA-CNMUUg6qhKPh3tSoJg.25MtqlVrCnM1OpDdOACgzA; sd_session_id=0e1c82089f7f754e317aac502e63709f9365gxrqa; id_ab=IDP; has_multiple_organizations=true; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-1124106680%7CMCIDTS%7C18864%7CMCMID%7C10640528059237186110715255087884724485%7CMCAID%7CNONE%7CMCOPTOUT-1629873064s%7CNONE%7CMCAAMLH-1630470664%7C3%7CMCAAMB-1630470664%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18716%7CvVersion%7C5.2.0%7CMCCIDH%7C-388222836; MIAMISESSION=99160783-9fb3-40af-bd9e-085d42705206:3807318670; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI3MzA5NCIsInRpbWVzdGFtcCI6MTYyOTg2NTg3MDgxN30=; s_pers=%20v8%3D1629866457031%7C1724474457031%3B%20v8_s%3DLess%2520than%25201%2520day%7C1629868257031%3B%20c19%3Dsd%253Abrowse%253Ajournalsandbooks%7C1629868257035%3B%20v68%3D1629865871934%7C1629868257046%3B; s_sess=%20s_cpc%3D0%3B%20c13%3Drelevance-desc%3B%20s_ppvl%3Dsd%25253Abrowse%25253Ajournalsandbooks%252C11%252C11%252C969%252C759%252C969%252C1920%252C1080%252C1%252CL%3B%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20c21%3Dno%2520criteria%2520set%2520%25E2%2580%2593%2520all%2520results%2520returned%3B%20e13%3Dno%2520criteria%2520set%2520%25E2%2580%2593%2520all%2520results%2520returned%253A%3B%20c7%3Dcontenttype%253Djl%3B%20e41%3D1%3B%20s_ppv%3Dsd%25253Abrowse%25253Ajournalsandbooks%252C53%252C11%252C969%252C759%252C969%252C1920%252C1080%252C1%252CL%3B',
    }


    response = requests.get('https://www.sciencedirect.com/search?qs='+ word, headers=headers, proxies={'https:': p.proxy}, timeout= 2)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.sciencedirect.com/search?qs=war', headers=headers)

            


userAgents = [ 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',                
                ]


def headers(): 
    ua = random.choice(userAgents)  
    headers = {
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-US,en;q=0.9',
                    'referer': 'https://www.google.com/',
                    'Upgrade-Insecure-Requests': '1',
                    "Accept-Encoding": "gzip, deflate", 
    }
    return headers


def proxy_generator():
    #response = requests.get("https://free-proxy-list.net/")
    #soup = BeautifulSoup(response.content, 'html.parser')
    #page= soup.find(text = "15")
    #page.click()
    proxies = []
    with open('C:/Users/Valued Client/Desktop/proxies.txt', 'r') as f:
        for line in f:
            proxies.append('https://' + line[:-1])
            #a = line
            
        

    proxy = random.choice(proxies)
    return proxy
        
        

    
    
    #proxy = {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}
    
    

def testProxy(proxies):
    a = False

    while a == False:
        
        try:
            #p = proxy_generator()
            p = random.choice(proxies)
            #print("Proxy currently being used: {}".format(p['proxy']))
            print(p.proxy + ': ')
            response = requests.get('https://free-proxy-list.net/', proxies={'https:':p.proxy} ,timeout=1)
            print('successful')
            a = True
            return p
            
            
            # if the request is successful, no exception is raised
        except:
            print( "                   Connection error ")
            pass
        


    


