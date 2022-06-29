import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')

link = soup.select('.titlelink')
link2 = soup2.select('.titlelink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_link = link + link2
mega_subtext = subtext + subtext2

def sort_by_vote(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'],reverse=True)

def custom_hn(link,subtext):
    hn = []
    for idx,item in enumerate(link):
        title = item.getText()
        href = item.get('href',None)
        votes = subtext[idx].select('.score')
        if len(votes):
         points = int(votes[0].getText().replace(' points',''))
         if points > 99:
          hn.append({'title':title,'link':href,'votes':points})
    return hn

pprint.pprint(custom_hn(mega_link,mega_subtext))
