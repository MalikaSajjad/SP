import requests
from PIL import Image
from bs4 import BeautifulSoup
from StringIO import StringIO
from datetime import datetime
import os
import json
import sys

def get_parser_obj(URL):
	try :
		req = requests.get(URL,stream =True)
		if req.status_code == 200:
			parser_obj = BeautifulSoup(req.content, "html.parser")
			return parser_obj
	except requests.ConnectionError:
		print("Connection error, Check your connection and try again :-)")
		sys.exit()

def next_page(sports_link):
	p_obj = get_parser_obj(sports_link)
	link_tag = p_obj.find("link",rel = "next")
	#print link_tag
	sports_link = link_tag['href']
	#print sports_link
	return sports_link

def get_sports_link(URL):
	parser_obj = get_parser_obj(URL)
	li_tag = parser_obj.find_all("li",id="menu-item-174055")
	#print li_tag
	for a_tag in li_tag[0]:
		sports_link = a_tag['href']
	#print sports_link
	return sports_link

def set_URL_list(URL,keywords): # set global list "links" with url(s) containing keywords	
	p_obj = get_parser_obj(URL)
	script = p_obj.find("script", type="application/ld+json")
	python_dict = json.loads(script.text)
	list_of_dict = python_dict["hasPart"]

	for dict_ in list_of_dict:
		for key in dict_.keys():
			if(str(key) == "url"): url = dict_[key]
			if(str(key) == "headline"):							
				if keywords in dict_[key].lower():
					links.append(str(url))
		
def handler(URL,keywords):
	url = get_sports_link(URL)
	set_URL_list(url,keywords)
	count = 0
	while(count < 4):
		url = next_page(url) 
		set_URL_list(url,keywords)
		count = count + 1
	return links

def main():
	URL = "https://propakistani.pk/"
	inp = raw_input("Enter the searching keywords : ")
	links = handler(URL, inp)
	print links



if __name__ == "__main__":
	links = []	# global list "'links' in globals()" 
	main()





