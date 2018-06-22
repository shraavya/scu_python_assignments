import urllib
import urllib2
from bs4 import BeautifulSoup
import wikipedia
import requests
from lxml import html
import json


#wiki = "https://en.wikipedia.org/wiki/Historical_components_of_the_Dow_Jones_Industrial_Average"

#page = urllib2.urlopen(wiki)
#soup = BeautifulSoup(page)
#print soup
#urllib2.HTTPError: HTTP Error 403: Forbidden

#table = soup.find("table", { "class" : "wikitable sortable" })
#print table


response = requests.get("https://en.wikipedia.org/wiki/Historical_components_of_the_Dow_Jones_Industrial_Average")
#print (response)
html_data = response.content

table_data = [[cell.text for cell in row("td")]
                         for row in BeautifulSoup(html_data,'lxml')("tr")]


print json.dumps(dict(table_data))
"""
page = html.fromstring(response.content)
print (page)
posts = page.cssselect('.table')
print (posts)
print (len(posts))
posts = page.xpath('//table [contains(@class, "wikitable")]')
print (posts)
print (len(posts))
posts = page.xpath('//h2[contains(@id, "September")]')
print (posts)
print (len(posts))
"""