from bs4 import BeautifulSoup

with open('tags.html','rt') as f:
    soup = BeautifulSoup(f,'html.parser')

article = soup.find('article', class_="single")

tags=[]
for tag in article.find_all('li'):
    tags.append(tag.a.text)
    #print(tag.a.text)

print(tags)


