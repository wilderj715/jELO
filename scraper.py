import requests
from bs4 import BeautifulSoup
from util import *

for year in range(startYear, endYear + 1):
	print "Gathering data for " + str(year)	
	
	for team in teamset:
		url = "https://www.pro-football-reference.com/\
		teams/" + team + "/" + str(year) + ".htm"

		page = requests.get(url)
		
		if page.status_code == 200:
			soup = BeautifulSoup(page.content, 'html.parser')
			tables = soup.find_all('div', {"class": "table_wrapper"})
		else:
			print "URL: " + url + " could not be reached!"
	#TODO: cache data to file to speed up processing times