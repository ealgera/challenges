from bs4 import BeautifulSoup

with open('rss.xml','rt') as f:
    soup = BeautifulSoup(f,'html.parser')

#print(soup.prettify())

categories = []
for item in soup.find_all('item'):
    for category in item.find_all("category"):
        categories.append(category.text)

print(categories)