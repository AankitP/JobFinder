#i am making a scraper for linkedin, to go through and find jobs available
#current goal:
#   Get the scraper finding jobs

#Future Goals:
#   Get it to search and filter for certain jobs
#   Get it to apply for me

#Data that I will grab from Linkedin for V1:
#   Job
#   Experience
#   required/preferred Skills
#   URL


#The imports
import requests
from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

#URL to Linkedin Jobs Page
url="https://www.linkedin.com/jobs/"

#requests for the results
results = requests.get(url)

#this is to make the content that we grabbed easier 
# to read by using Beautiful Soup
soup = bs(results.text, "html.parser")

with open("output.txt", "w") as f:
    f.write(soup.prettify())
