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

seed = 'https://www.cpp.edu/sci/computer-science/'

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
        
    

def crawlerThread(frontier):
    while not frontier.done():
        url = frontier.next_url()
        html = urlopen(url)

frontier = Frontier(seed)
crawlerThread(frontier)