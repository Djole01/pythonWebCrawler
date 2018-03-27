import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 0
    while page <= max_pages:
        # url of the page to crawl, note: preferably with "page" at the end.
        url = 'https://www.amazon.co.uk/s/ref=lp_61_pg_2?rh=n%3A266239%2Cn%3A%211025612%2Cn%3A61&page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.find_all('a',{'class':'a-link-normal'}):
            if not (link.string):
                page = page

            elif "Kindle" in link.string:
                page = page
            elif "Hardcover" in link.string:
                page = page
            elif "Audio" in link.string:
                page = page

            elif "Paperback" in link.string:
                page = page
            elif "CD-ROM" in link.string:
                page = page
            elif "£" in link.string:
                page = page
            elif "See more" in link.string:
                page = page

            else:
                    href = "www.amazon.co.uk" + link.get('href')
                    title = link.string
                    print(title)
                    print(href)
        #page += 1




trade_spider(2)