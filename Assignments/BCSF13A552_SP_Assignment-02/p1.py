##python script that downloads last 26 mp3 files of all Qaris from given link:https://download.quranicaudio.com/quran/
##and merge all 26 mp3 files and make a single file with the name of second_Half.mp3

import requests
from PIL import Image
from bs4 import BeautifulSoup
from StringIO import StringIO
from datetime import datetime
import os
import urllib

def get_mp3(URL):

	req = requests.get(URL,stream =True)
	mp3_links = []
	if req.status_code == 200:
		parser_obj = BeautifulSoup(req.content, "html.parser")
		href_tag_list = parser_obj.find_all("a")
		for href_tag in href_tag_list[1:]:
			mp3_links.append(href_tag['href'])
	return mp3_links

def download_mp3(url_list):
	count = 0
	mypath = "/home/malika/SP/Assignments/Assignment2/p1/"
	for mp3_url in url_list:
		URL = "https://download.quranicaudio.com/quran/"+mp3_url
		mp3_links = get_mp3(URL)
		mp3_links = mp3_links[-26:]
		dir_ = mypath+mp3_url[:-1]
		os.mkdir(dir_)
		os.chdir(dir_)

		f = open(dir_+"/logFile", "a+")
		f.write("%s Total Qari %d\n"%(date().strip("\n"),len(url_list)))
		count = count + 1
		f.write("%s Start Processing %d out %d\n" %(date().strip("\n"),count,len(url_list)))
		f.write("%s "%(date().strip("\n")))
		f.write(u'{0}'.format(mp3_url[:-1]))		
		for i in mp3_links:
			f.write("%s "%(date().strip("\n")))
			f.write(u'{0}'.format(mp3_url[:-1]))
			f.write(" %s START\n"%(i)) 
			os.system('wget -c "{}" '.format("https://download.quranicaudio.com/quran/"+mp3_url+i))
			f.write("%s "%(date().strip("\n")))
			f.write(u'{0}'.format(mp3_url[:-1]))
			f.write(" %s END\n"%(i))  
		f.write("%s Merging the files of "%(date().strip("\n")))
		f.write(u'{0}'.format(mp3_url[:-1]))
		f.write(" START\n")
		os.system('mp3wrap second_Half.mp3 *.mp3')
		f.write("%s Merging the files of "%(date().strip("\n")))
		f.write(u'{0}'.format(mp3_url[:-1]))
		f.write(" END\n")
		f.close()		
		os.chdir(mypath)


def date():
	return os.popen('date').read()		

def main():
	URL = "https://download.quranicaudio.com/quran/"
	url_list = get_mp3(URL)
	download_mp3(url_list)

if __name__ == "__main__":
	main()













