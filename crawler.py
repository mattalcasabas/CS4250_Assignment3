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
import re


class Frontier:
    def __init__(self):
        # list holding sites to visit
        self.to_visit = []
        # set holding already visited sites
        self.visited = set()
        self.is_done = False
    
    def add_url(self, url):
        # check to see if url has been added to list already
        if url not in self.visited and url not in self.to_visit:
            self.to_visit.append(url)

    def next_url(self):
        # return the next url in the list
        if self.to_visit:
            return self.to_visit.pop(0)
        return None
    
    def mark_visited(self, url):
        # mark a url as visited
        self.visited.add(url)

    def done(self):
        # check if crawling through frontier is complete, either by checking flag or checking if to_visit empty
        return self.is_done or not self.to_visit
    
    def clear_frontier(self):
        # clears the frontier and sets is_done flag to true
        self.to_visit.clear()
        self.is_done = True

def is_target_page(url):
    return url == target

def retrieve_url(url):
    try:
        html = urlopen(url).read().decode('utf-8')
        return html
    except HTTPError as e:
        print(f"Failed to connect: {url} ({e})")
        return None


        
def store_page(url, html):
    # save the given page as html in MongoDB
    document = {
        "url": url,
        "html": html
    }
    db.collection.insert_one(document)

def parse(html):
    bs = BeautifulSoup(html, 'html.parser')
    # return all links found with <a href=> tag in HTML
    return [a['href'] for a in bs.find_all('a', href = True)]

def flag_target_page(url):
    print(f"Found target page: {url}")

def crawlerThread(frontier):
    while not frontier.done():
        url = frontier.next_url()
        if not url:
            continue
        print(f"Current page: {url}")
        html = retrieve_url(url)
        # skip the page if urlopen returns an error
        if html is None:
            continue
        store_page(url, html)
        frontier.mark_visited(url)

        if is_target_page(url):
            flag_target_page(url)
            frontier.clear_frontier()
            break
        else:
            for link in parse(html):
                # if we have a relative link, add the base url to it
                if link.startswith('/'):
                    match = re.match(r"^(https?://[^/]+)", url)
                    if match:
                        base_url = match.group(1)
                        link = f"{base_url}{link}"
                # skip over any non-HTTP or non-HTTPS links
                if not link.startswith('http'):
                    continue
                frontier.add_url(link)

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client.cs4250_assign3
    collection = db.pages
    seed = 'https://www.cpp.edu/sci/computer-science/'
    target = 'https://www.cpp.edu/sci/computer-science/faculty-and-staff/permanent-faculty.shtml'
    frontier = Frontier()
    frontier.add_url(seed)
    crawlerThread(frontier)