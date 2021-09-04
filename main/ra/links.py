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


def springer(word, proxy, refType): #articles
    
    springers = []
    springLinks = []
    
    if refType == 'article':

        response = requests.get('https://www.springeropen.com/search?query=' + word + '&searchType=publisherSearch', headers = headers(), proxies={'https:': proxy}, timeout=2) #articles 
        soup = BeautifulSoup(response.content, 'html.parser')

    
        a= soup.find('ol', class_='c-list-group c-list-group--bordered c-list-group c-list-group--md')

        if a != None: #find ol tag where naa ang rows sa list
            bb = a.findAll('li') #find li tag where nag contain sa rows

            for b in bb:
            
                            
                article = b.find('article') #find article tag
                if article != None:

                    div = article.find('div', class_='u-mb-16') #find div tag
                    a = div.h3  # extract title
                    p = div.find('p', class_='c-listing__authors u-mb-0') #extract authors
                    z = []
                                        
                    z.append(a.text) # store title to list
                    z.append(div.p.text) # store description of link to list
                    z.append(p.text) # store author to list
                    div2 = article.find('div',class_='c-meta')
                    z.append(div2.text) # store date&type to list

                    springLinks.append(a.a['href']) # extract link and store to list
                    
                    springers.append(z)
    else:
        response = requests.get('https://www.springer.com/gp/search?query=' + word + '&submit=Submit', headers = headers(), proxies={'https:': proxy}, timeout=2) #books
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find('div', id='result-list')
        
        if rows != None:

            for a in range(22):
                z = []
                books1 = rows.find('div', class_='result-item result-item-' + str(a) + ' result-type-book')
                books2 = rows.find('div', class_='result-item result-item-' + str(a) + ' result-type-book last')
                editorial = rows.find('div', class_='result-item result-item-' + str(a) + ' result-type-editorial')

                if editorial != None:
                    z.append(editorial.h4.a.text) #title
                    z.append(editorial.div.text) #desicription
                    springLinks.append(editorial.h4.a['href'])
                    
                elif books1 != None:
                    
                    z.append(books1.h4.a.text) #title
                    z.append(books1.p.text) #author
                    z.append(books1.div.text) #desicription
                    z.append(books1.find('p', class_='format').text) #format
                    #z.append(books1.find('p', class_='price-container price-loaded').span.text) #price
                    springLinks.append(books1.h4.a['href'])
     
                elif books2 != None:
                    z.append(books2.h4.a.text) #title
                    z.append(books2.p.text) #author
                    z.append(books2.div.text) #desicription
                    z.append(books2.find('p', class_='format').text) #format
                    #z.append(books2.find('p', class_='price-container price-loaded').text) #price
                    springLinks.append(books2.h4.a['href'])

                springers.append(z)

    return springers, springLinks


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

def scirp(word, proxy, refType):
    
    scirp = []
    scirpLinks = []         
    
    if refType == 'article':
        response = requests.get('https://www.scirp.org/journal/articles.aspx?searchcode='+ word+'&searchfield=All&page=1&skid=59931926', headers = headers(), proxies={'https:': proxy}, timeout=2) #books                         #
    else:
        response = requests.get('https://www.scirp.org/journal/articles.aspx?searchcode='+ word +'&searchfield=jname&page=1&skid=0', headers = headers(), proxies={'https:': proxy}, timeout=2) #books
    soup = BeautifulSoup(response.content, 'html.parser')
    a=soup.find('ul', class_='list-unstyled list_link').findAll('li')
   
    for i in a:
        z = []
        x = i.find('div', class_='list_unit') #get container of rows
        z.append(i.div.text) # get title
        z.append(i.find('div', class_='list_author').text) #author 
        z.append(i.find('div', class_='list_unit').text.replace('¼Œ', ' ')) #get other info
        z.append(i.find('div', class_='list_doi').text) 
        scirp.append(z)
        scirpLinks.append(i.div.span.a['href'])

    return scirp, scirpLinks

        

def practice(proxy): #books

    with open ('"C:/Users/Valued Client/Desktop/html/tandfonlineArticles.html"', 'r', errors='ignore') as html_file:   
        content = html_file.read()
        soup = BeautifulSoup(content, 'html.parser')
        
            

    #print(a)
                    
    #for x in z:
        #print(x)
        
    
    
   


    
def scienceDirect(word,proxy, refType):
    scienceDirects = []
    scienceLinks = []
    #ua = random.choice(userAgents) 

    headers = {
    'authority': 'www.sciencedirect.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://id.elsevier.com/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'EUID=80a39c81-5643-43a6-a14d-dbdeb3ff56f9; acw=09351bde6bf54645d9782c50aec0216b3d8fgxrqb%7C%24%7C7FE5B9DF2B3037D1D537624359B49D59B548D9F405B982A584FFE088DD21B3F5910D2AC152F178678A72C4EF7F838BCFF3A6BCE916C7220C0E9169905BBD791CB0469A67597464825D387A21AFA2E514; fingerPrintToken=304bf7913ab704ec79a638d26e517201; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; mbox=session%2302abf4c3d6134b1dbb91254aec108e20%231630677951%7CPC%2302abf4c3d6134b1dbb91254aec108e20.34_0%231693920891; __cf_bm=mkqBWvPVt7LqWoplsj8oKRa4zOmQgbbP.mFFSjMq_W8-1630676090-0-Ab2T7/CPzvqT2PiDxe2vwcXqyRck184flU0KOHSLpuxb4Kv/OkQmAlUeeW1k/1yWsj1z2il0PBbVb3he/P3aKMifihTV99xGCnfKYB6WzH3V; sd_access=eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P1c4whQcaIcZIW1VjPMdyw.07ypbH8eqzTpCvbZAxlUElHNWX05_zuLhXPG9TmPcfnXTPewtpjhmn7vlS-8GtrcJCBtOuf9-SEb3UhXj44c9KthDGtnp17rOOXu5-cFeA5tgzQG40z5ACFs-gcNb0YT8Gzd-j_t4GqF0Zotxxb6MQ.O9y8cW2ugwKQ-YO1jtIrDg; sd_session_id=2ba5055895ae144ff2087ca994c018919258gxrqb; id_ab=IDP; has_multiple_organizations=true; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-1124106680%7CMCIDTS%7C18873%7CMCMID%7C81261105090677501200180261852203688591%7CMCAID%7CNONE%7CMCOPTOUT-1630683383s%7CNONE%7CMCAAMLH-1631280983%7C3%7CMCAAMB-1631280983%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCCIDH%7C-388222836%7CvVersion%7C5.2.0; MIAMISESSION=48480567-060c-4f77-bc44-3d8dd08d5a19:3808128993; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI3MzA5NCIsInRpbWVzdGFtcCI6MTYzMDY3NjE5MzE4Mn0=; s_pers=%20v8%3D1630676196943%7C1725284196943%3B%20v8_s%3DLess%2520than%25201%2520day%7C1630677996943%3B%20c19%3Dsd%253Abrowse%253Ajournalsandbooks%7C1630677996950%3B%20v68%3D1630676196692%7C1630677996963%3B; s_sess=%20s_cpc%3D0%3B%20c21%3Dno%2520criteria%2520set%2520%25E2%2580%2593%2520all%2520results%2520returned%3B%20e13%3Dno%2520criteria%2520set%2520%25E2%2580%2593%2520all%2520results%2520returned%253A%3B%20c7%3Dcontenttype%253Djl%3B%20s_sq%3D%3B%20s_ppvl%3Dsd%25253Abrowse%25253Ajournalsandbooks%252C11%252C11%252C969%252C1461%252C969%252C1920%252C1080%252C1%252CP%3B%20e41%3D1%3B%20s_cc%3Dtrue%3B%20s_ppv%3Dsd%25253Abrowse%25253Ajournalsandbooks%252C11%252C11%252C969%252C1007%252C969%252C1920%252C1080%252C1%252CP%3B',
    }


    if refType == 'journal':
        response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=JL&searchPhrase='+ word, headers=headers, proxies={'https:': proxy}, timeout= 2)
    elif refType == 'book':
        response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=BK&searchPhrase='+ word, headers=headers, proxies={'https:': proxy}, timeout= 2)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    lli= soup.findAll('li', class_='publication branded u-padding-xs-ver js-publication')

    for li in lli:
        z = []
                    #scienceDTitles.append(li.a.text)
        z.append(li.a.text)
        p = li.div.p
        pp = li.div.find('p', class_='u-display-inline u-clr-grey8')

        if refType == 'journal':
            if pp != None:
                ppp = pp.find('span')
                            #scienceDDescriptions.append(p.text + " ● " + ppp.text)
                z.append( "Journal ● " + ppp.text)
            else:
                z.append( "Journal")
        if refType == 'book':

            z.append(li.p.text)
            z.append(li.div.text)



        scienceLinks.append(li.a['href'])
        scienceDirects.append(z)
        #print(soup.find('a', text='Sign in'))
   
    return scienceDirects, scienceLinks

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
                    'referer': 'https://google.com/',
                    'Upgrade-Insecure-Requests': '1',
                     

                     
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
        


    


