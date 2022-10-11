################################################################
#This is only me following a tutorial
#on how to make a webscraper to scrape movie details
#https://hackernoon.com/how-to-build-a-web-scraper-with-python-step-by-step-guide-jxkp3yum
################################################################

#The imports
import requests
from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

#This is to make sure I only get US english movies
headers = {"Accept-Language": "en-us, en;q=0.5"}

#URL of the site
url="https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv&ref=hackernoon.com"

#requests for the results
results = requests.get(url, headers=headers)

#this is to make the content that we grabbed easier 
# to read by using Beautiful Soup
soup = bs(results.text, "html.parser")

# print(soup.prettify()) #prints soup in a more readable format

#This is to store the data for the movies
Movies = {}

#Tell the scraper to find all of the lister-item mode-advanceed divs
movie_div = soup.find_all('div', class_='lister-item mode-advanced')

#initiate the for loop
#this tells scraper to iterate through
#every div container we stored in movie_div
for container in movie_div:
    name = container.h3.a.text
    # titles.append(name)

    #h3 is attribute notation, which tells the scraper to access the tag
    #find() is a method we will use to access this particular <span> tag
    #(‘span’, class_ = ‘lister-item-year’) is the distinctive <span> tag we want
    year = container.h3.find('span', class_='lister-item-year').text
    # years.append(year)

    #find() is what we will use to find the <span>
    #if container.p.find('span', class_='runtime') else '' says if there is data, we will grab it
    #text tells the scraper to grab the stext from the <span> tag
    runtime = container.find('span', class_='runtime').text if container.p.find('span', class_='runtime') else ''
    # time.append(runtime)

    a = {year, runtime}
    
    Movies[name] = a

for i in Movies:
    print(f"{i}:{Movies[i]}")