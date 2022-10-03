import requests
from bs4 import BeautifulSoup
from csv import writer
from langdetect import detect
def trade_spider(max_pages):
    page = 1
    with open('test2.csv', 'w', encoding = 'utf8', newline='') as f:
        thewriter = writer(f)
        header = ['title', 'abstract', 'keyphrases']
        thewriter.writerow(header)
        while page <= max_pages:
            # url = "https://www.freelancer.com/jobs/php/"+str(page)+"/?languages=en&fixed=true&hourly=true"
            url = "https://www.freelancer.com/jobs/"+str(page)+"/?fixed=true&hourly=true&languages=en"
            print( url)
            source_code = requests.get( url )
            print( source_code)
            plain_text =  source_code.text
            soup = BeautifulSoup(plain_text, features="html.parser")
            
            # for link in soup.findAll('a', {'class': 'JobSearchCard-primary-heading-link'}):
            titles = soup.findAll('a', {'class': 'JobSearchCard-primary-heading-link'})
            abstracts = soup.findAll('p', {'class': 'JobSearchCard-primary-description'})
            keyphrases = soup.findAll('div', {'class': 'JobSearchCard-primary-tags'})
            i = 0
            for link, link1, link3 in zip (titles, abstracts,  keyphrases ):
                childrens = link3.children
                phrase = ""
                for children in childrens:
                    if children != '\n':
                        child = children.string
                        child = child.strip()
                        phrase += child+", "
                # print(phrase.strip(", ") )
                i+=1
                print("ok"+str(i))
                phrase = phrase.strip(", ")
                title = link.string
                abstract = link1.string
             
                title = title.strip()
                if not abstract:
                    abstract = "Empty String"
                else:
                    abstract = " ".join(abstract.split())
                    # lang = detect(abstract)
                    # if lang == 'en':
                    #     abstract = abstract.strip()
                    # else:
                    #     abstract = "Language Error"
        
                info = [title, abstract, phrase]
                thewriter.writerow(info)
                # print(title)
            page += 1

trade_spider(20)