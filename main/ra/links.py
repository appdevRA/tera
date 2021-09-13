        #with open ('C:/Users/Valued Client/Desktop/html/springerBooks.html', 'r', errors='ignore') as html_file:
        #content = html_file.read()
        #print(content)
        #soup = BeautifulSoup(content, 'html.parser')
import bs4
from bs4 import BeautifulSoup
import os
import requests
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import random
import time


def springer(word, proxy, refType): #articles
    
    springers = []
    springLinks = []
    
    if refType == 'article':
        x = False
        while(x == False):
            try:
                response = requests.get('https://www.springeropen.com/search?query=' + word + '&searchType=publisherSearch', headers = headers(), proxies={'https:': proxy}, timeout=2) #articles 
                x = True
            except ConnectionError:
                print('connection error')
            except ConnectTimeout:
                response =  requests.get('https://www.springeropen.com/search?query=' + word + '&searchType=publisherSearch', headers = headers(), proxies={'https:': proxy}, timeout=2) #articles             
                x = True
                print('olok')
        
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
        x = False
        while(x == False):
            try:
                response = requests.get('https://www.springer.com/gp/search?query=' + word + '&submit=Submit', headers = headers(), proxies={'https:': proxy}, timeout=2) #books
                x = True
                
            except ConnectTimeout:
                response = requests.get('https://www.springer.com/gp/search?query=' + word + '&submit=Submit', headers = headers(), proxies={'https:': proxy}, timeout=2) #books
                print('connection timeout')
                x = True

            except ConnectionError:
                print('connection Error')
        
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


def scienceDirect(word,proxy, refType):
    scienceDirects = []
    scienceLinks = []
    #ua = random.choice(userAgents) 

    headers = {
    'authority': 'www.sciencedirect.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Microsoft Edge";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://id.elsevier.com/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'EUID=80a39c81-5643-43a6-a14d-dbdeb3ff56f9; mboxes=%7B%22universal-view-pdf%22%3A%7B%22variation%22%3A%22B%22%7D%7D; utt=ae01-efa25bdbb71478802a627452c2319959fc3-A; __cf_bm=Cs3AllVLvfExI.GD9S4YrOjA7KKpAZMsvwss2c_gRBQ-1631066905-0-Ab63xE2w0UU0/Jov8DAGqKwjeWjuvVBiSoc241moMepvXFJxc4cbwD8pFL1i8nOas29TvVqcN++WQC1nKFDkrM1p9fbnjoPe01oAE8oc0X0l; fingerPrintToken=4a7c35f82ff0bfa77f2a77051cace374; acw=3bc2ead93a0ea54e245b60947fce7822e6d0gxrqa%7C%24%7CCC8D6A441741955B0496C5C0029BEB33E459BC75294B406422D12FA5EED074331B812E9FC23CEF97D38B5F5C03AFFB1DFF0197EF7049CD583FBA44D1BD4E4F2EB0469A67597464825D387A21AFA2E514; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; mbox=session%231777de9d91174694b72619ed2c22deea%231631068782%7CPC%231777de9d91174694b72619ed2c22deea.37_0%231694311722; sd_access=eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..UB275g-40bVgfsqkN9FDHQ.q7ZbARkzP1lIvVdviGHYy1Lcu-a3HtMrw4-8DDzyIhfsBLhAGmJ9R6I9gY1DF4xqd-HF4G5loABeoJtUBWHgLIf1AgpRQpXfvycQ_6jYFb2LcOOKBJmVquXtcI-p-fM_pmIu0c2P3ARetnysOo43WQ.WSOQZdxDeStJd73AMSP3CQ; sd_session_id=269052942e4b304813685ea259926c78f5aegxrqa; id_ab=IDP; has_multiple_organizations=true; MIAMISESSION=e2da1f14-4d22-4756-ae1d-bfd060718d7a:3808519743; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI3MzA5NCIsInRpbWVzdGFtcCI6MTYzMTA2Njk0MzU3Mn0=; s_pers=%20v8%3D1631066946556%7C1725674946556%3B%20v8_s%3DLess%2520than%25201%2520day%7C1631068746556%3B%20c19%3Dsd%253Ahome%253Ahpx%7C1631068746576%3B%20v68%3D1631066943693%7C1631068746594%3B; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-1124106680%7CMCIDTS%7C18879%7CMCMID%7C81261105090677501200180261852203688591%7CMCAID%7CNONE%7CMCOPTOUT-1631074146s%7CNONE%7CMCAAMLH-1631671746%7C3%7CMCAAMB-1631671746%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCCIDH%7C-388222836%7CvVersion%7C5.2.0; s_sess=%20s_sq%3D%3B%20s_ppvl%3D%3B%20e41%3D1%3B%20s_cpc%3D0%3B%20s_cc%3Dtrue%3B%20s_ppv%3Dsd%25253Ahome%25253Ahpx%252C22%252C22%252C969%252C1456%252C969%252C1920%252C1080%252C1%252CP%3B',
    }
    x = False
    while(x == False):
        try:
            if refType == 'journal':
                response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=JL&searchPhrase='+ word, headers=headers, proxies={'https:': proxy}, timeout= 5)
                x = True
            elif refType == 'book':
                response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=BK&searchPhrase='+ word, headers=headers, proxies={'https:': proxy}, timeout= 5)
                x = True
        except ConnectionError:
                print('connection error')
        except ConnectTimeout: 
            if refType == 'journal':
                response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=JL&searchPhrase='+ word, headers=headers, proxies={'https:': proxy}, timeout= 5)
                x = True
                print('connection timeout')
            elif refType == 'book':
                response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=BK&searchPhrase='+ word, headers=headers, proxies={'https:': proxy}, timeout= 5)
                x = True
                print('connection timeout')
        
    
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
        else:
            if(li.p.text != 'Book'):
                z.append(li.p.text)
            z.append(li.div.text)



        scienceLinks.append(li.a['href'])
        scienceDirects.append(z)
        #print(soup.find('a', text='Sign in'))
   
    return scienceDirects, scienceLinks


def scirp(word, proxy, refType):
    
    scirp = []
    scirpLinks = []         
    
    x = False
    while(x == False):
        try:
            if refType == 'article':
                response = requests.get('https://www.scirp.org/journal/articles.aspx?searchcode='+ word+'&searchfield=All&page=1&skid=59931926', headers = headers(), proxies={'https:': proxy}, timeout=4) #books                         #
                x = True
            else:
                response = requests.get('https://www.scirp.org/journal/articles.aspx?searchcode='+ word +'&searchfield=jname&page=1&skid=0', headers = headers(), proxies={'https:': proxy}, timeout=3) #books
                x = True
        except ConnectTimeout:
            if refType == 'article':
                response = requests.get('https://www.scirp.org/journal/articles.aspx?searchcode='+ word+'&searchfield=All&page=1&skid=59931926', headers = headers(), proxies={'https:': proxy}, timeout=4) #books                         #
                x = True
            else:
                response = requests.get('https://www.scirp.org/journal/articles.aspx?searchcode='+ word +'&searchfield=jname&page=1&skid=0', headers = headers(), proxies={'https:': proxy}, timeout=3) #books
                x = True
        except ConnectionError:
                print('connection error')

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

def tandFOnline(word, proxy, refType): #books

    results= []
    links = []
        
    
    
    if refType == 'article':
        x = False
        while(x == False):
            
            try:
                response = requests.get('https://www.tandfonline.com/action/doSearch?AllField=' + word, headers = headers(), proxies={'https:': proxy}, timeout=3) #books
                x = True

            except ConnectTimeout:
                response = requests.get('https://www.tandfonline.com/action/doSearch?AllField=' + word, headers = headers(), proxies={'https:': proxy}, timeout=3) #books
                x = True
            except ConnectionError:
                print('connection error')
            

        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.findAll('article', class_='searchResultItem')

        for row in rows:
            z=[]
            z.append(row.find('a', class_='ref nowrap').text) #title
            z.append(row.find('div', class_='author').text) #author
            z.append(row.find('div', class_='publication-meta').text) #others
            z.append(row.find('span', class_='publication-year').text) #date

            
            results.append(z)
                    #links.append(container.find('a', class_='ref nowrap')['href'])
            links.append(row.find('a', class_='ref nowrap')['href'])
        return results, links

    else:
        x = False
        while(x == False):
            
            try:
                response = requests.get('https://www.tandfonline.com/action/doSearch?AllField='+ word +'&startPage=&target=titleSearch&content=title' , headers = headers(), proxies={'https:': proxy}, timeout=2) #books
                x = True
            except ConnectTimeout:
                response = requests.get('https://www.tandfonline.com/action/doSearch?AllField='+ word +'&startPage=&target=titleSearch&content=title' + word, headers = headers(), proxies={'https:': proxy}, timeout=2) #books
                print('connection timeout')
                x = True
            except ConnectionError:
                print('connection error')

        soup = BeautifulSoup(response.content, 'html.parser')
        rows =soup.findAll('li', class_='searchResultItem browse-result')

        for row in rows:
            z = []
            z.append(row.find('a', class_='ref').text) #title
            z.append(row.find('h3').text)

            results.append(z)
            links.append(row.find('a', class_='ref')['href'])
        return results, links

    

def practice(word, proxy, refType):
    results = []
    links = []
    x = False
    while(x == False):
        try:
            if refType == 'article':
                response = requests.get('https://www.ncbi.nlm.nih.gov/pmc/?term='+ word, headers = headers(), proxies={'https:': proxy}, timeout=3) #books                                       
                x = True
            else:
                response = requests.get('https://www.ncbi.nlm.nih.gov/books/?term='+ word, headers = headers(), proxies={'https:': proxy}, timeout=3) #books 
                x = True
        except ConnectTimeout:
            if refType == 'article': 
                response = requests.get('https://www.ncbi.nlm.nih.gov/pmc/?term='+ word, headers = headers(), proxies={'https:': proxy}, timeout=3) #books 
                x = True
            else:
                response = requests.get('https://www.ncbi.nlm.nih.gov/books/?term='+ word, headers = headers(), proxies={'https:': proxy}, timeout=3) #books   
                x = True
        except ConnectionError:
                print('connection error')

    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.findAll('div', class_='rslt')
        
    if refType == 'article':
        for row in rows:
            z = []
            
            z.append(row.find('div', class_='title').a.text)
            z.append(row.find('div', class_='desc').text)
            z.append(row.find('div', class_='details').text)
            z.append(row.find('div', class_='resc').text)

            results.append(z)
            links.append(row.find('div', class_='title').a['href'])

       
    else:
        for row in rows:
            z = []
            z.append(row.find('div', class_='rsltcont').p.text.replace('â€“', '-').replace('.','')) #title
            if row.find('div', class_='rsltcont').find('p', class_='desc').text != '': 
                z.append(row.find('div', class_='rsltcont').find('p', class_='desc').text)  #description
            z.append(row.find('div', class_='rsltcont').find('p', class_='details').text.replace('.','')) #place
            

            results.append(z)
            links.append(row.find('div', class_='rsltcont').p.a['href'])

    
    return results, links

        
        
            


def proxy_generator():

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
        


    


