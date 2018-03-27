# pythonWebCrawler
a python webcrawler, that returns all the links along with a title from an amazon products page.

This is a program I made when I was around 15 years  old in Highschool. I came back and revisited it and made it compatible for amazon
book section. To use it, change the url variable in crawler.py to the url you wish to use. As an example I have used amazon book products.

The bug/issue I have with it is that after the for loop, "adding : pages += 1" does not work as intended. 
Therefore my program only works for the first page of the amazon book section. 
With this bug fixed, it would be able to crawl links and titles from multiple pages.
