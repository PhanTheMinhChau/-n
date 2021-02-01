from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from requests import get
import os
import shutil
import re

url = []
f = open("data.txt", "r")
data = f.readlines()
f.closed
time = (int(data[0])/60)
url.append(data[1])
d = datetime.today() + timedelta(hours=0, minutes=time)

if os.path.isdir(os.getcwd()+"\\thư mục chứa file"):
    shutil.rmtree(os.getcwd()+"\\thư mục chứa file")

os.mkdir("thư mục chứa file")
add = os.getcwd()
url_goc = url[0]


def link(ad):
    web = get(ad)
    soup = BeautifulSoup(web.text, 'html.parser')
    results = soup('a', attrs={'href': True})
    for i in results:
       a = i['href']
       link_chuan = f'^{url_goc}[^?#]*$'
       link_thieu = '^/[^?#]*$'
       if re.match(link_chuan, a):
           if url.count(a) == 0:
               url.append(a)
       else:
           if re.match(link_thieu, a):
               url_chuan = f'{url_goc}{a}'
               if url.count(url_chuan) == 0:
                   url.append(url_chuan)


n=1
for item in url:
        if d <= datetime.now():
            break
        page = get(item)
        soup = BeautifulSoup(page.text,"html.parser" )
        title = str(soup.title.string)
        link(item)
        titles = title.replace("|", "_").replace("/", "").replace('"', "").replace('\t',"").replace("?", "")
        html = soup.prettify()
        os.chdir(add+"\\thư mục chứa file")
        try:
            f = open("file"+str(n)+"-"+titles+".html","x",encoding="utf-8")
            f.write(html)
        except:
            f = open("file"+str(n))
            f.write(html)
        os.chdir(add)
        n = n+1