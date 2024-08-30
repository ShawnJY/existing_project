import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.com/'
r = requests.get(url)
print(r) #get 200 means succefully connected

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class' : 'post-title'})
#print(title) #will get alot of messy title with link
#title[0].getText() #This get only one title but still not only text
title1 = title[0].getText()
print(title1) #this will get perfect text title only

for t in title:
    print(t.getText()) #for loop get all title in text