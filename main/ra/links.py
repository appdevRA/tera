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

def springerss(word, proxy):
    response = requests.get('https://www.springeropen.com/search?query=' + word + '&searchType=publisherSearch', headers = headers(), proxies={'https:': proxy}, timeout=5) #articles

    #response = requests.get('https://www.springer.com/gp/search?query=' + word + '&submit=Submit', headers = headers(), proxies={'https:': proxy}, timeout=5) #books
    #print(response.json())  
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def springer(word, proxy, refType): #articles
    
    springers = []
    springLinks = []
    
    if refType == 'article':

        response = requests.get('https://www.springeropen.com/search?query=' + word + '&searchType=publisherSearch', headers = headers(), proxies={'https:': proxy}, timeout=5) #articles 
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
        response = requests.get('https://www.springer.com/gp/search?query=' + word + '&submit=Submit', headers = headers(), proxies={'https:': proxy}, timeout=5) #books
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


def springerasdsad(): #books
    with open ('C:/Users/Valued Client/Desktop/html/springerBooks.html', 'r', errors='ignore') as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content, 'html.parser')
        rows = soup.find('div', id='result-list')
        springers = []
        springLinks = []

        for a in range(22):
            z = []
            books1 = rows.find('div', class_='result-item result-item-' + str(a) + ' result-type-book')
            books2 = rows.find('div', class_='result-item result-item-' + str(a) + ' result-type-book last')
            editorial = rows.find('div', class_='result-item result-item-' + str(a) + ' result-type-editorial')

            if editorial != None:
                z.append(editorial.h4.text) #title
                z.append(editorial.div.text) #desicription
                springLinks.append(editorial.h4.a['href'])
                
            elif books1 != None:
                
                z.append(books1.h4.text) #title
                z.append(books1.p.text) #author
                z.append(books1.div.text) #desicription
                z.append(books1.find('p', class_='format').text) #format
                z.append(books1.find('p', class_='price-container price-loaded').text) #price
                springLinks.append(books1.h4.a['href'])
 
            elif books2 != None:
                z.append(books2.h4.text) #title
                z.append(books2.p.text) #author
                z.append(books2.div.text) #desicription
                z.append(books2.find('p', class_='format').text) #format
                z.append(books2.find('p', class_='price-container price-loaded').text) #price
                springLinks.append(books2.h4.a['href'])

            springers.append(z)
    return springers, springLinks


                

        
        
    
   


    
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
    'cookie': 'EUID=75fdfe63-504d-4c8a-8180-c03a43da237c; utt=2146-84ee935a77144283645aebe835a645e74f7-M0M6; mboxes=%7B%22universal-view-pdf%22%3A%7B%22variation%22%3A%22B%22%7D%2C%22article-page-remote-access-button-location-server-side-mbox%22%3A%7B%22variation%22%3A%22D%22%7D%7D; mbox=session%23caaef878370e46848c55649e062d0920%231629869107%7CPC%2370b4195123dc401fa07762b437030b81.34_0%231693112047; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; fingerPrintToken=304bf7913ab704ec79a638d26e517201; __cf_bm=2eb341bbac40850d99d61d983fc98c4fb1b7e555-1630330507-1800-AeR2kGyV+RiD/8aC9qFGUZlzy3GykJeCrQtC7hj1AmIQXgijzHiT6FO4j1uy0pXQMCXOgGzxI4w2lcHyoxh90hONGCbtCkZVsLt2YXMnv+cp; acw=3e48fa7d9805d64b41693ab7f5916c9de7f9gxrqa%7C%24%7CFDE57228A87A1E921752A73B15806CC60269982D4900291F8E47168FD4362AB30D5534CDD14CD24C2E6E2566651B09047BABD03304DD6A6B3FBA44D1BD4E4F2EB0469A67597464825D387A21AFA2E514; sd_access=eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..uv09-FeH3kJYTB6FJ3PRBQ.Wy2wQ4ZC35w0mtcYg2mfW7RIyV3L9hW7y8mIw3Dot-W0DHm0JCqa1uI-NTtV4Mw1TXsYnB0PizuB6iAeAjfJ4nvkSkpGGznfiW7zAD7sh1d0qcBHZetXvkdB5GYw_3ST4l9Wi0LYgsXIWSTPI0Ux0w.InDQbrelQ9dNWKSIF5My7w; sd_session_id=f5ba213d23c77548428adf91c02028be90ccgxrqa; id_ab=IDP; has_multiple_organizations=true; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-1124106680%7CMCIDTS%7C18870%7CMCMID%7C10640528059237186110715255087884724485%7CMCAID%7CNONE%7CMCOPTOUT-1630337925s%7CNONE%7CMCAAMLH-1630935525%7C3%7CMCAAMB-1630935525%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18716%7CvVersion%7C5.2.0%7CMCCIDH%7C-388222836; MIAMISESSION=f5be2c16-3f68-4de3-b140-c795b4b26ef5:3807783526; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI3MzA5NCIsInRpbWVzdGFtcCI6MTYzMDMzMDcyNjQ0NH0=; s_pers=%20v8%3D1630330728674%7C1724938728674%3B%20v8_s%3DLess%2520than%25201%2520day%7C1630332528674%3B%20c19%3Dsd%253Ahome%253Ahpx%7C1630332528679%3B%20v68%3D1630330726557%7C1630332528693%3B; s_sess=%20s_cpc%3D0%3B%20c7%3Dcontenttype%253Djl%3B%20c21%3Dno%2520criteria%2520set%2520%25E2%2580%2593%2520all%2520results%2520returned%3B%20e13%3Dno%2520criteria%2520set%2520%25E2%2580%2593%2520all%2520results%2520returned%253A%3B%20s_sq%3D%3B%20s_ppvl%3Dsd%25253Ahome%25253Ahpx%252C43%252C43%252C969%252C759%252C969%252C1920%252C1080%252C1%252CL%3B%20e41%3D1%3B%20s_cc%3Dtrue%3B%20s_ppv%3Dsd%25253Ahome%25253Ahpx%252C43%252C43%252C969%252C759%252C969%252C1920%252C1080%252C1%252CL%3B',
    }






    if refType == 'journal':
        response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=JL&searchPhrase='+ word, headers=headers, proxies={'https:': proxy}, timeout= 5)
    else:
        response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=BK&searchPhrase='+ word, headers=headers, proxies={'https:': proxy}, timeout= 2)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    lli= soup.findAll('li', class_='publication branded u-padding-xs-ver js-publication')

    for li in lli:
        z = []
                    #scienceDTitles.append(li.a.text)
        z.append(li.a.text)
        p = li.div.p
        pp = li.div.find('p', class_='u-display-inline u-clr-grey8')

        if pp != None:
            ppp = pp.find('span')
                        #scienceDDescriptions.append(p.text + " ● " + ppp.text)
            z.append( "Journal ● " + ppp.text)
        elif li.div.text != None:
            z.append(li.div.text)



        scienceLinks.append(li.a['href'])
        scienceDirects.append(z)

   
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
                    'referer': 'https://springeropen.com/',
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
        


    


