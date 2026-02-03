import requests
from bs4 import BeautifulSoup
from lxml import etree

article_res=requests.get("https://github.com/shreyajadhav157/Project.git")
articles_soup=BeautifulSoup(article_res.text,'html.parser')

# change beautifulsoup into xml Element object
tree=etree.HTML(str(articles_soup))

article=articles_soup.find('h1',id='maincontent')
article_title=article.text.strip()

article_author=tree.xpath('/html/body/div[1]/section[3]/div/div[2]/div[1]/div/div[1]/div[2]/a/span')[0].text.strip()
article_updated_data=tree.xpath('/html/body/div[1]/section[3]/div/div[2]/div[1]/div/div[2]/div[2]')[0].text.strip()

print(f'The title of the article is:{article_title},written by:{article_author}, {article_updated_data}')

paragraphs = articles_soup.find("div", class_="article__content").find_all(class_="paragraph")
for p in paragraphs:
    print(p.text.strip())
