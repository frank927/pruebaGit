import requests
from bs4 import BeautifulSoup
import random

agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
]
user_agent = random.choice(agent_list)

data=[]

url="https://github.com/frank927"

page = requests.get(url, user_agent)

soup = BeautifulSoup(page.text, 'html.parser')

noticias = soup.find_all('span', {'class':'repo'})
  
for d in noticias:

     data.append(d.text)
     
print(data)

print (len(data))