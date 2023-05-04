import requests
from bs4 import BeautifulSoup

url = "https://atilsamancioglu.com/"

foundLinks = []


def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")
    return soup

def crawl(url):
    links = make_request(url)
    for link in links.findAll("a"):
        foundLink = link.get("href")
        if "#" in foundLink:
            foundLink = foundLink.split("#")[0]
        if url in foundLink and foundLink not in foundLinks:
            foundLinks.append(foundLink)
            print(foundLink)
            #recursive
            crawl(foundLink)

print(crawl(url))