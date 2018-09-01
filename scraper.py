import requests
from bs4 import BeautifulSoup

# Subject to change ...
url = "https://www.pro-football-reference.com/teams/nwe/2017.htm"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tables = soup.find_all('div', {"class": "table_wrapper"})
tablecount = 0

if page.status_code == 200:
	print "Data retrieved from " + url + " successfully!"
else:
	print "URL: " + url + " could not be reached!"

for t in tables:
	tablecount+=1

print "tablecount: " + str(tablecount)