# procedure crawlerThread (frontier)
    # while not frontier.done() do
        # url <— frontier.nextURL()
        # html <— retrieveHTML(url)
        # storePage(url, html)
        # if target_page (parse (html))
            # flagTargetPage(url)
            # clear_frontier()
        # else
            # for each not visited url in parse (html) do
                # frontier.addURL(url)
            # end for
    # end while
# end procedure

from urllib.request import urlopen
from bs4 import BeautifulSoup
from pymongo import MongoClient
from urllib.error import HTTPError


client = MongoClient('mongodb://localhost:27017/')
db = client.cs4250_assign3
collection = db.pages
seed = 'https://www.cpp.edu/sci/computer-science/'
target = 'https://www.cpp.edu/sci/computer-science/faculty-and-staff/permanent-faculty.shtml'

class Frontier:
    def __init__(self, seed_url):
        self.seed_url = seed_url
        # initialize url_list as a dictionary:
        # key: url
        # value: false if not tagged, true if tagged
        self.url_list = {}
        self.url_list[seed_url] = False
    
    def done(self):
        return not bool(self.url_list)
    
    def add_url(self, url):
        self.url_list[url] = False

    def flag_target_page(self, url):
        self.url_list[url] = True

    def clear_frontier(self):
        self.url_list.clear()
        
def store_page(url, html):
    # save the given page as html in MongoDB
    document = {
        "url": url,
        "html": html
    }
    db.collection.insert_one(document)

def target_page(html, target):
    # use BeautifulSoup to find <a> tags
    bs = BeautifulSoup(html, "html.parser")
    links = bs.find_all("a")

def crawlerThread(frontier):
    while not frontier.done():
        url = frontier.next_url()
        html = urlopen(url)
        store_page(url, html)

frontier = Frontier(seed)
crawlerThread(frontier)