        #with open ('C:/Users/Valued Client/Desktop/UA.html', 'r', errors='ignore') as html_file:
        #content = html_file.read()
        #print(content)
        #soup = BeautifulSoup(content, 'html.parser')
import bs4
from bs4 import BeautifulSoup
import os
import requests
import random


#from fake_user_agent import UserAgent
        

def springer(word, proxy):
    
    
    #response = data_scraper('get', 'https://www.springeropen.com/search?query=' + word + '&searchType=publisherSearch', headers = headers())
    response = requests.get('https://www.springeropen.com/search?query=' + word + '&searchType=publisherSearch', headers = headers(), proxies={'https:': proxy}, timeout=5)
    #print(response.json())  
    soup = BeautifulSoup(response.content, 'html.parser')
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


def practice(p):
    headers = {
        'authority': 'www.sciencedirect.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.sciencedirect.com/search?articleTypes=FLA&lastSelectedFacet=articleTypes&qs=war',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'EUID=75fdfe63-504d-4c8a-8180-c03a43da237c; utt=2146-84ee935a77144283645aebe835a645e74f7-M0M6; mboxes=^%^7B^%^22universal-view-pdf^%^22^%^3A^%^7B^%^22variation^%^22^%^3A^%^22B^%^22^%^7D^%^2C^%^22article-page-remote-access-button-location-server-side-mbox^%^22^%^3A^%^7B^%^22variation^%^22^%^3A^%^22D^%^22^%^7D^%^7D; acw=4e1e78732a03e249022a0fd5b2feb508dd95gxrqb^%^7C^%^24^%^7CFE7D4FD9788B1C39FEC533964C0094FB1AC98DAA5A5176A57BEFB8F56164C34B3EC83BF485FFFD0CA1F7AB7A55E837097DD5F08DD7A895C20E9169905BBD791CB0469A67597464825D387A21AFA2E514; mbox=session^%^23e7585ea25ab6444dae178e8f7680b6a8^%^231629353135^%^7CPC^%^2370b4195123dc401fa07762b437030b81.34_0^%^231692596075; fingerPrintToken=3e3740303850eda319ffaf58b07f6772; AMCVS_4D6368F454EC41940A4C98A6^%^40AdobeOrg=1; sd_access=eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..q_RRkOk5c0k6eLm_TymCHQ.msUjSm_ZRz7B9AxeVXKJtGjndkuqDVMH7dNMVgcmtYs5xW0qm1GH21QiIEV0y8cz6Cj7ePrRuni0ivbsJ3sus9pxPDvAK2pN6CZ7kquYMG-MXB5Cnh8kzYyEfD5ODiADcqGtIcRg4cmdAQ6Z1OJP2Q.6KlczdfoZwvV25Er7QpmyA; sd_session_id=f4c10dac71052543fa68369217a29fff6150gxrqb; id_ab=IDP; __cf_bm=43a0fed4d1b774551d61b7b90dd5f5e789223b96-1629353558-1800-AeehFg0E7Mqbw8GTOz19ffI1k82oVyBg/jsGrpvc4CJ6z6VOW2YmjGLfaCGA+s1ufEo1yVuJygC988+l0nk0WPgDEROFVwN3zlizUSwVKFmq; has_multiple_organizations=true; AMCV_4D6368F454EC41940A4C98A6^%^40AdobeOrg=-1124106680^%^7CMCIDTS^%^7C18858^%^7CMCMID^%^7C10640528059237186110715255087884724485^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1629360763s^%^7CNONE^%^7CMCAAMLH-1629958363^%^7C3^%^7CMCAAMB-1629958363^%^7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI^%^7CMCSYNCSOP^%^7C411-18716^%^7CvVersion^%^7C5.2.0^%^7CMCCIDH^%^7C-388222836; MIAMISESSION=d4034143-2f60-4fb9-bb2f-1b09c02b9c31:3806806377; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI3MzA5NCIsInRpbWVzdGFtcCI6MTYyOTM1MzU3NzEwM30=; s_pers=^%^20v8^%^3D1629353580478^%^7C1723961580478^%^3B^%^20v8_s^%^3DLess^%^2520than^%^25207^%^2520days^%^7C1629355380478^%^3B^%^20c19^%^3Dsd^%^253Ahome^%^253Ahpx^%^7C1629355380485^%^3B^%^20v68^%^3D1629353577233^%^7C1629355380498^%^3B; s_sess=^%^20s_cpc^%^3D0^%^3B^%^20c21^%^3Dqs^%^253Dwar^%^3B^%^20e13^%^3Dqs^%^253Dwar^%^253A1^%^3B^%^20c13^%^3Drelevance-desc^%^3B^%^20c7^%^3Darticletypes^%^253Dresearch^%^2520articles^%^3B^%^20s_ppvl^%^3Dsd^%^25253Asearch^%^25253Aresults^%^25253Acustomer-standard^%^252C100^%^252C100^%^252C969^%^252C759^%^252C969^%^252C1920^%^252C1080^%^252C1^%^252CL^%^3B^%^20e41^%^3D1^%^3B^%^20s_sq^%^3D^%^3B^%^20s_cc^%^3Dtrue^%^3B^%^20s_ppv^%^3Dsd^%^25253Ahome^%^25253Ahpx^%^252C43^%^252C43^%^252C969^%^252C759^%^252C969^%^252C1920^%^252C1080^%^252C1^%^252CL^%^3B',
    }


    

    response = requests.get('https://www.sciencedirect.com/search?qs=avengers&articleTypes=FLA&lastSelectedFacet=articleTypes', headers=headers, proxies={'https:': p.proxy})

    

    #response = requests.get('https://www.sciencedirect.com/search?qs=avengers', headers=headers, proxies={'https:': p.proxy}, timeout= 3)
    a = response.status_code
    print(a)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.prettify())
    #print(response)
   


    
def scienceDirect(p):
    word = 'respiratory'
    ua = random.choice(userAgents) 
    headers = {
        'authority': 'www.sciencedirect.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': ua, #'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.sciencedirect.com/search?articleTypes=FLA&lastSelectedFacet=articleTypes&qs=war',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'EUID=75fdfe63-504d-4c8a-8180-c03a43da237c; utt=2146-84ee935a77144283645aebe835a645e74f7-M0M6; mboxes=^%^7B^%^22universal-view-pdf^%^22^%^3A^%^7B^%^22variation^%^22^%^3A^%^22B^%^22^%^7D^%^2C^%^22article-page-remote-access-button-location-server-side-mbox^%^22^%^3A^%^7B^%^22variation^%^22^%^3A^%^22D^%^22^%^7D^%^7D; acw=4e1e78732a03e249022a0fd5b2feb508dd95gxrqb^%^7C^%^24^%^7CFE7D4FD9788B1C39FEC533964C0094FB1AC98DAA5A5176A57BEFB8F56164C34B3EC83BF485FFFD0CA1F7AB7A55E837097DD5F08DD7A895C20E9169905BBD791CB0469A67597464825D387A21AFA2E514; mbox=session^%^23e7585ea25ab6444dae178e8f7680b6a8^%^231629353135^%^7CPC^%^2370b4195123dc401fa07762b437030b81.34_0^%^231692596075; fingerPrintToken=3e3740303850eda319ffaf58b07f6772; AMCVS_4D6368F454EC41940A4C98A6^%^40AdobeOrg=1; sd_access=eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..q_RRkOk5c0k6eLm_TymCHQ.msUjSm_ZRz7B9AxeVXKJtGjndkuqDVMH7dNMVgcmtYs5xW0qm1GH21QiIEV0y8cz6Cj7ePrRuni0ivbsJ3sus9pxPDvAK2pN6CZ7kquYMG-MXB5Cnh8kzYyEfD5ODiADcqGtIcRg4cmdAQ6Z1OJP2Q.6KlczdfoZwvV25Er7QpmyA; sd_session_id=f4c10dac71052543fa68369217a29fff6150gxrqb; id_ab=IDP; __cf_bm=43a0fed4d1b774551d61b7b90dd5f5e789223b96-1629353558-1800-AeehFg0E7Mqbw8GTOz19ffI1k82oVyBg/jsGrpvc4CJ6z6VOW2YmjGLfaCGA+s1ufEo1yVuJygC988+l0nk0WPgDEROFVwN3zlizUSwVKFmq; has_multiple_organizations=true; AMCV_4D6368F454EC41940A4C98A6^%^40AdobeOrg=-1124106680^%^7CMCIDTS^%^7C18858^%^7CMCMID^%^7C10640528059237186110715255087884724485^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1629360763s^%^7CNONE^%^7CMCAAMLH-1629958363^%^7C3^%^7CMCAAMB-1629958363^%^7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI^%^7CMCSYNCSOP^%^7C411-18716^%^7CvVersion^%^7C5.2.0^%^7CMCCIDH^%^7C-388222836; MIAMISESSION=d4034143-2f60-4fb9-bb2f-1b09c02b9c31:3806806377; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI3MzA5NCIsInRpbWVzdGFtcCI6MTYyOTM1MzU3NzEwM30=; s_pers=^%^20v8^%^3D1629353580478^%^7C1723961580478^%^3B^%^20v8_s^%^3DLess^%^2520than^%^25207^%^2520days^%^7C1629355380478^%^3B^%^20c19^%^3Dsd^%^253Ahome^%^253Ahpx^%^7C1629355380485^%^3B^%^20v68^%^3D1629353577233^%^7C1629355380498^%^3B; s_sess=^%^20s_cpc^%^3D0^%^3B^%^20c21^%^3Dqs^%^253Dwar^%^3B^%^20e13^%^3Dqs^%^253Dwar^%^253A1^%^3B^%^20c13^%^3Drelevance-desc^%^3B^%^20c7^%^3Darticletypes^%^253Dresearch^%^2520articles^%^3B^%^20s_ppvl^%^3Dsd^%^25253Asearch^%^25253Aresults^%^25253Acustomer-standard^%^252C100^%^252C100^%^252C969^%^252C759^%^252C969^%^252C1920^%^252C1080^%^252C1^%^252CL^%^3B^%^20e41^%^3D1^%^3B^%^20s_sq^%^3D^%^3B^%^20s_cc^%^3Dtrue^%^3B^%^20s_ppv^%^3Dsd^%^25253Ahome^%^25253Ahpx^%^252C43^%^252C43^%^252C969^%^252C759^%^252C969^%^252C1920^%^252C1080^%^252C1^%^252CL^%^3B',
    }

    response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=JL&searchPhrase=' + word , headers=headers, proxies={'https:': p.proxy}, timeout= 2)

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
        


    


