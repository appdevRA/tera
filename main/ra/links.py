        #with open ('C:/Users/Valued Client/Desktop/html/springerBooks.html', 'r', errors='ignore') as html_file:
        #content = html_file.read()
        #print(content)
        #soup = BeautifulSoup(content, 'html.parser')
        #
import bs4
from bs4 import BeautifulSoup
import os
import requests
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import random
import time





def scrape(word, proxy, refType, pageNumber, site, header):


    if site == 'Springeropen.com':
        return springer(word, proxy, refType,pageNumber)
    elif site == 'Sciencedirect.com':
        return scienceDirect(word, proxy, refType, pageNumber, header)
    elif site == 'Scirp.org':
        return scirp(word, proxy, refType, pageNumber)
    elif site == 'tandfonline':
        return tandFOnline(word, proxy, refType, pageNumber)
    elif site == 'herdin':
        return herdin(word, proxy, refType, pageNumber)
    elif site == 'zLibrary':
        return zLibrary(word, proxy, refType, pageNumber)






def springer(word, proxy, refType, pageNumber): # INDEX 1 STARTING SA PAGINATION DIRI
    
    springers = []
    springLinks = []
    
    if refType == 'article':
        x = False
        while(x == False):
            try:
                response = requests.get('https://www.springeropen.com/search?searchType=publisherSearch&sort=Relevance&query=' + word +'&page='+ str(pageNumber), headers = headers(), proxies={'https:': proxy}, timeout=2) #articles 
                x = True
            except ConnectionError:
                print('Connection Error')
                return False

            except ConnectTimeout:
                print('Connect Timeout')
                
            except ReadTimeout:
                print('except')
        
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
                                        
                    z.append(a.text.replace('\n','')) # store title to list
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
                response = requests.get('https://www.springer.com/gp/search?dnc=true&facet-type=type__book&page='+ str(pageNumber) +'&query='+ word+'&submit=Submit', headers = headers(), proxies={'https:': proxy}, timeout=2) #books
                x = True
                
            except ConnectionError:
                print('Connection Error')
                return False

            except ConnectTimeout:
                print('Connect Timeout')
                
            except ReadTimeout:
                print('except')
        
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
                    springLinks.append('https://www.springer.com' +books1.h4.a['href'])
     
                elif books2 != None:
                    z.append(books2.h4.a.text) #title
                    z.append(books2.p.text) #author
                    z.append(books2.div.text) #desicription
                    z.append(books2.find('p', class_='format').text) #format
                    #z.append(books2.find('p', class_='price-container price-loaded').text) #price
                    springLinks.append('https://www.springer.com' +books2.h4.a['href'])

                springers.append(z)

    
    return springers, springLinks

def details(link, proxy, refType ):
    ref = refType.split(' ')
    if refType == 'Springeropen.com Article':
        # with open ('C:/Users/Valued Client/Desktop/html/sprigner DETAILS.html', 'r', errors='ignore') as html_file:
        #     content = html_file.read()
            # soup = BeautifulSoup(content, 'html.parser')
        
        # reference = refType.split(' ')
      
        response = requests.get('https:'+link,headers=headers(), proxies={'https:': proxy})
        soup = BeautifulSoup(response.content, 'html.parser')
        descrip = soup.find('div', class_='c-article-section__content').p.text
        description = descrip[:500]
        # print(len(description))
        # if len(description) > 1000:
        #     a = soup.find('h3', text='Conclusion')
        #     print(a.next)
      
        details={
            'websiteTitle': ref[0],
            'itemType': ref[1],
            'author': soup.find('div', class_='c-article-header').find('ul', class_='c-article-author-list js-etal-collapsed').text,
            'description': description,
            'journalItBelongs': soup.find('i', attrs={'data-test':'journal-title'}).text,
            'volume': soup.find('b', attrs={'data-test':'journal-volume'}).text[7:],
            'publishYear': soup.find('span', class_="c-bibliographic-information__value").text,
            'doi': soup.find('a', attrs={'data-track-action':'view doi'}).text, 
            'subtitle':'',
            'citation':'',
            'downloads':'',
            'publisher':'',
            'edition':'',
            'pages':''
            
        }
        

            
        # websiteTitle = refType[0]
        # itemType = refType[1]
        
        return details

    elif refType == 'Springeropen.com Book':
        response = requests.get(link + '#about',headers=headers(), proxies={'https:': proxy})
        soup = BeautifulSoup(response.content, 'html.parser')

        if soup.find('div', class_='unique-selling-points unique-selling-points--collapsed u-mb-36') == None:
            description = ''
        else:
            description = soup.find('div', class_='unique-selling-points unique-selling-points--collapsed u-mb-36').text

        if soup.find('span', id='bookcitations-count-number') == None:
            cite = ''
        else:
            cite = soup.find('span', id='bookcitations-count-number').text
        
        if soup.find('h2', class_='page-title__subtitle') == None:
            subtitle = ''
        else:
            subtitle = soup.find('h2', class_='page-title__subtitle').text

        if soup.find('h1', attrs={"itemprop":"name"}) == None:
            if soup.find('h1', class_='app-journal-header__title') == None:
                title = ''
            else:
                title= soup.find('h1', class_='app-journal-header__title').text
        else:
            title= soup.find('h1', attrs={"itemprop":"name"}).text
        details={
            'websiteTitle': ref[0],
            'itemType': ref[1],
            'title': title,
            'subtitle': subtitle,
            'description': description,
            'citation': cite,
            'downloads': soup.find('span', class_='test-metric-count article-metrics__views').text,
            'author': soup.find('ul', class_='test-contributor-names').text,
            'publisher': soup.find('span', attrs={"itemprop":"name"}).text,
            'edition': soup.find('span', id='edition-number').text,
            'pages': soup.find('span', id='number-of-pages').text,
            'doi': soup.find('span', id='doi-url').text,
            'journalItBelongs': '',
            'volume': '',
            'publishYear': '',


            
        }

        return details


def scienceDirect(word,proxy, refType, pageNumber, header):
    scienceDirects = []
    scienceLinks = []
    #ua = random.choice(userAgents) 

    
    x = False
    while(x == False):
        try:
            if refType == 'journal':
                response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=JL&searchPhrase='+ word, headers=header, proxies={'https:': proxy}, timeout= 5)
                x = True
            else:
                response = requests.get('https://www.sciencedirect.com/browse/journals-and-books?contentType=BK&searchPhrase='+ word, headers=header, proxies={'https:': proxy}, timeout= 5) # books
                x = True
        except ConnectionError:
                print('Connection Error')
                return False

        except ConnectTimeout:
            print('Connect Timeout')
                
        except ReadTimeout:
            print('except')
        
    
    soup = BeautifulSoup(response.content, 'html.parser')
    lli= soup.findAll('li', class_='publication branded u-padding-xs-ver js-publication')

    for li in lli:
        z = []
                    
        z.append(li.a.text)
        p = li.div.p
        pp = li.div.find('p', class_='u-display-inline u-clr-grey8') 

        if refType == 'journal':
            if pp != None:
                ppp = pp.find('span')
                            
                z.append( "Journal ● " + ppp.text)
            else:
                z.append( "Journal")
        else:
            if(li.p.text != 'Book'):
                z.append(li.p.text)
            z.append(li.div.text)



        scienceLinks.append('https://www.sciencedirect.com/' + li.a['href'])
        scienceDirects.append(z)

    if(soup.find('a', text='Sign in')):
        print("Cookies expired")
    else:
        print("Cookies not expired")
   
    return scienceDirects, scienceLinks


def scirp(word, proxy, refType, pageNumber):
    
    scirp = []
    scirpLinks = []         
    
    x = False
    while(x == False):
        try:
            if refType == 'article':
                response = requests.get('https://www.scirp.org/journal/articles.aspx?searchcode='+ word+'&searchfield=All&page=1', headers = headers(), proxies={'https:': proxy}, timeout=2) # article                   #
                x = True
            else:
                response = requests.get('https://www.scirp.org/journal/articles.aspx?searchcode='+ word +'&searchfield=jname&page=1&skid=0', headers = headers(), proxies={'https:': proxy}, timeout=2) #journal
                x = True
        except ConnectionError:
            print('Connection Error')
            return False

        except ConnectTimeout:
            print('Connect Timeout')
                
        except ReadTimeout:
            print('ReadTimeout')
        

    soup = BeautifulSoup(response.content, 'html.parser')
    a=soup.find('ul', class_='list-unstyled list_link').findAll('li')
   
    for i in a:
        z = []
        x = i.find('div', class_='list_unit') #get container of rows
        z.append(i.div.text) # get title
        z.append(i.find('div', class_='txt5').text) #author 
        z.append(i.find('div', class_='list_unit').text.replace('¼Œ', ' ')) #get other info
        z.append(i.find('div', class_='list_doi').text) 
        scirp.append(z)

        
        scirpLinks.append('https://www.scirp.org/journal/' + i.div.span.a['href'])

    return scirp, scirpLinks








def tandFOnline(word, proxy, refType, pageNumber): # INDEX ZERO MAG START ILANG PAGE

    results= []
    links = []
        
    
    
    if refType == 'article':
        x = False
        while(x == False):
            
            try:
                response = requests.get('https://www.tandfonline.com/action/doSearch?AllField='+ word +'&pageSize=10&subjectTitle=&startPage='+ str(pageNumber), headers = headers(), proxies={'https:': proxy}, timeout=3) # article
                x = True
            except ConnectionError:
                print('Connection Error')
                return False

            except ConnectTimeout:
                print('Connect Timeout')
                
            except ReadTimeout:
                print('except')
                
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.findAll('article', class_='searchResultItem')

        for row in rows:
            z=[]
            z.append(row.find('a', class_='ref nowrap').text) #title
            z.append(row.find('div', class_='author').text) #author
            z.append(row.find('div', class_='publication-meta').text) #others
            z.append(row.find('span', class_='publication-year').text) #date

            
            results.append(z)
            links.append('https://www.tandfonline.com' + row.find('a', class_='ref nowrap')['href'])
        return results, links

    elif refType == 'journal':
        x = False
        while(x == False):
            
            try:
                response = requests.get('https://www.tandfonline.com/action/doSearch?AllField='+ word +'&target=titleSearch&content=title&pageSize=10&subjectTitle=&startPage='+str(pageNumber) , headers = headers(), proxies={'https:': proxy}, timeout=3) # journals
                x = True
            except ConnectionError:
                print('Connection Error')
                return False

            except ConnectTimeout:
                print('Connect Timeout')
                
            except ReadTimeout:
                print('Read Timeout')

        soup = BeautifulSoup(response.content, 'html.parser')
        rows =soup.findAll('li', class_='searchResultItem browse-result')

        for row in rows:
            z = []
            z.append(row.find('a', class_='ref').text) #title
            z.append(row.find('h3').text)

            results.append(z)
            links.append('https://www.tandfonline.com' + row.find('a', class_='ref')['href'])
        return results, links

    elif refType == 'database':
        x = False
        while(x == False):
            
            try:
                response = requests.get('https://www.tandfonline.com/action/doSearch?AllField='+ word +'&content=db&target=database&pageSize=10&subjectTitle=&startPage='+ str(pageNumber) , headers = headers(), proxies={'https:': proxy}, timeout=3) # journals
                x = True
            except ConnectionError:
                print('Connection Error')
                return False

            except ConnectTimeout:
                print('Connect Timeout')
                
            except ReadTimeout:
                print('except')

        soup = BeautifulSoup(response.content, 'html.parser')
        rows =soup.findAll('article', class_='searchResultItem')

        for row in rows:
            z = []
            z.append(row.find('a', class_='ref').text) #title
            z.append(row.find('span', class_='entryAuthor search-link hlFld-ContribAuthor').text) # author
            z.append(row.find('div', class_='publication-meta').text) # source

            results.append(z)
            links.append('https://www.tandfonline.com' + row.find('a', class_='ref')['href'])
        return results, links


    



        
def herdin(word, proxy,refType, pageNumber): # INDEX ZERO ANG STARTING SA ILA PAGINATION
    results = []
    links = []
    x = False
    while(x == False):
        try:
            if refType == 'journal':
                response = requests.get('https://www.herdin.ph/index.php?option=com_herdin&view=publiclistowp&layout=list&type=researches&searchstr='+ word +'&res_source=journal&start=' + pageNumber, headers = headers(), proxies={'https:': proxy}, timeout=3) #article                                       
                x = True
            elif refType == 'book' :
                response = requests.get('https://www.herdin.ph/index.php?option=com_herdin&view=publiclistowp&layout=list&type=researches&searchstr='+ word + '&res_source=book&start=' + pageNumber, headers = headers(), proxies={'https:': proxy}, timeout=3) #books 
                x = True
            elif refType == 'research project' :
                response = requests.get('https://www.herdin.ph/index.php?option=com_herdin&view=publiclistowp&layout=list&type=researches&searchstr='+ word + '&res_source=research_project&start=' + pageNumber, headers = headers(), proxies={'https:': proxy}, timeout=3) #books 
                x = True
            elif refType == 'resident research' :
                response = requests.get('https://www.herdin.ph/index.php?option=com_herdin&view=publiclistowp&layout=list&type=researches&searchstr='+ word + '&res_source=resident_research&start=0'+ pageNumber, headers = headers(), proxies={'https:': proxy}, timeout=3) #books 
                x = True
            elif refType == 'thesis' :
                response = requests.get('https://www.herdin.ph/index.php?option=com_herdin&view=publiclistowp&layout=list&type=researches&searchstr='+ word + '&res_source=thesis/dissertation&start=0' + pageNumber, headers = headers(), proxies={'https:': proxy}, timeout=3) #books 
                x = True

        except ConnectionError:
            print('Connection Error')
            return False

        except ConnectTimeout:
            print('Connect Timeout')
                
        except ReadTimeout:
            print('Read timeout')

    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.findAll('div',attrs={'style':'overflow: hidden; padding-left: 5px;'})

    
    for row in rows:
        z = []
        z.append(row.find('h4', attrs={'style':'line-height:1.5; text-align:justify;'}).text) # title

        if row.find('div', attrs={'name':'opt1'}) != None:
            z.append(row.find('div', attrs={'name':'opt1'}).text.replace('\n','').replace('\xa0','')) # author

        z.append(row.find('div', attrs={'name':'opt2'}).text.replace('\n','').replace('\xa0','')) # source

        if row.find('div', attrs={'name':'opt3'}) != None:
            z.append(row.find('div', attrs={'name':'opt3'}).text.replace('\n','').replace('\xa0','')) # abstract

        z.append(row.find('div', attrs={'name':'opt4'}).text.replace('\n','').replace('\xa0','')) # others
        z.append(row.find('div', attrs={'name':'opt5'}).text.replace('\n','').replace('\xa0','')) # author

        results.append(z)

        links.append('https://www.ncbi.nlm.nih.gov' + row.find('h4', attrs={'style':'line-height:1.5; text-align:justify;'}).a['href'])
            
    return results, links


def zLibrary(word, proxy,refType, pageNumber):

    results = []
    links = []

    x = False
    while(x == False):
        try:
            if refType == 'article':
                response = requests.get('https://booksc.org/s/'+ word, headers = headers(), proxies={'https:': proxy}, timeout=2) # article
                x = True
            elif refType == 'book':
                response = requests.get('https://1lib.ph/s/'+ word, headers = headers(), proxies={'https:': proxy}, timeout=2) #books 
                x = True
        except ConnectionError:
            print('Connection Error')
            return False

        except ConnectTimeout:
            print('Connect Timeout')
                
        except ReadTimeout:
            print('Read Timeout')
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    if refType == 'book':
        rows = soup.findAll('td', attrs={'style':'vertical-align: top;'})

        for row in rows:
            z= []
            z.append(row.find('h3', attrs={'itemprop':'name'} ).text.replace('\n','')) # title
            z.append(row.find('div', class_='authors' ).text) #author
            if row.find('div', attrs={'title':'Publisher'} ) != None:
                z.append(row.find('div', attrs={'title':'Publisher'} ).text) # publisher
            z.append(row.find('div', class_='bookDetailsBox').text)
            
            results.append(z)
            links.append('https://1lib.ph/' + row.find('h3', attrs={'itemprop':'name'}).a['href'])

        return results, links


    elif refType == 'article':
        rows = soup.findAll('tr',class_='bookRow')

        for row in rows:
            z= []
            z.append(row.find('h3', attrs={'itemprop':'name'} ).text.replace('\n','').replace('â€“','-')) # title

            z.append(row.find('div', class_='authors' ).text) #author

            if row.find('div', attrs={'title':'Publisher'} ) != None:
                z.append(row.find('div', attrs={'title':'Publisher'} ).text) # publisher

            z.append(row.find('div', class_='bookDetailsBox').div.text.replace('\n',' ')) # journal of the 

            stringPosition = row.find('div', class_='bookDetailsBox').text.find('Year')
            z.append(row.find('div', class_='bookDetailsBox').text[stringPosition:].replace('\n',' ')) # journal of the 

            results.append(z)
            links.append('https://booksc.org/' + row.find('h3', attrs={'itemprop':'name'}).a['href'])
            
            
        return results, links

            






    



def proxy_generator1():

    response = requests.get('https://www.proxynova.com/proxy-server-list/country-ph/', headers = headers())
    soup = BeautifulSoup(response.content, 'html.parser')
    
        
    page= soup.find('textarea', class_='form-control')
    a =page.text
    proxies = a[75:].split("\n")
    #print(proxies)
    print(proxies)
    return proxies


def proxy_generator2():
    proxies = []
    
    for x in range(2):
        
        headers = {
        'authority': 'www.proxyhub.me',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.proxyhub.me/en/ph-https-proxy-list.html',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '__gads=ID=6c6661a0f109efd0-2246a8b0b9cc0070:T=1634804154:RT=1634804154:S=ALNI_MZZ5TnlvEI8S1B6-41Yln5ggLyG4A; page='+ str(x+1) +'; anonymity=all',
        }

        response = requests.get('https://www.proxyhub.me/en/ph-https-proxy-list.html', headers = headers)
        soup = BeautifulSoup(response.content, 'html.parser')
     
        rows = soup.find('tbody').findAll('tr')
         
        for row in rows:
            z = []
            x = 0
            columns = row.findAll('td')
            for column in columns:
                if x >= 2:
                    break
                
                z.append(column.text.replace(' ', '').replace('\n', ''))
                if(z[0] != '' and len(z) == 1):
                    z.append(":")
                x += 1
           
            if len(z) > 1: 
                proxies.append(''.join(z)) 
        print("Number of proxies extracted: ",len(proxies))
        time.sleep(10)
       

    proxyList = list(dict.fromkeys(proxies))
    # print(proxyList[91])

    return proxyList
    

   

    

    #with open('C:/Users/Valued Client/Desktop/proxies.txt', 'w') as file:    / writing in a file /
    
    #with open ('C:/Users/Valued Client/Desktop/free proxy.html', 'r', errors='ignore') as html_file:   / opening a file /
            #content = html_file.read()
            #soup = BeautifulSoup(content, 'html.parser')

        #response = requests.get("https://free-proxy-list.net/")
        #soup = BeautifulSoup(response.content, 'html.parser')
        ##mylist = list(dict.fromkeys(mylist))
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


    

def testProxy(proxies, ptype):
    a = False

    while a == False:

        if ptype == 1:
            try:
                p = random.choice(proxies)
                print(p.proxy + ': ')
                response = requests.get('https://google.com', proxies={'https:':p.proxy} ,timeout=1)
                print('new proxy assigned')
                a = True
                return p.proxy
            except:
                print( "                   Connection error ")
                pass
        else:
            try:
                response = requests.get('https://free-proxy-list.net/', proxies={'https:':proxies} ,timeout=1)
                print(proxies + ' working\n')
                a = True
                return proxies
            except:
                print(proxies,' not working\n')
                return False
        
            
            # if the request is successful, no exception is raised
       
        

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
    


