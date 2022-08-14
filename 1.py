import requests
from bs4 import  BeautifulSoup
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

save_dir = "D:\\ai\\豪婿关系\\"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

url = "http://www.shuquge.com/txt/99462/index.html"
req  = requests.get(url = url ,headers = headers)
req.encoding = 'utf-8'
html = BeautifulSoup(req.text,'lxml')
dd_list = html.find_all('dd')
print(dd_list)

def GetOneChart():
    url = "http://www.shuquge.com/txt/99462/24031460.html"
    req  = requests.get(url = url ,headers = headers)
    req.encoding = 'utf-8'
    html = BeautifulSoup(req.text,'lxml')
    h1_list = html.find('h1')
    div_list = html.find_all('div', class_ = 'showtxt')
    name = h1_list.string
    print(div_list[0].text)
    filename = save_dir + "/" + "%s.txt"%name
    print(filename)
    with open(filename, "w", encoding="utf-8") as file:
         file.write(div_list[0].text)
         file.close()
