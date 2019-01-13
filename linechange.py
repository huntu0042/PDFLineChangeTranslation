# -*- coding: utf-8 -*-

import os,time
import requests 

'''
import sys
from bs4 import BeautifulSoup
import urllib, urllib2
'''

from googletrans import Translator 



FILENAME = "cp.txt"
OUTFILE = "out.txt"

pdftext = open(FILENAME,'r')
pdfall = pdftext.read()
pdflines = pdftext.readlines()


newall = ""

count = 0

print(len(pdfall))


for i in range(0,len(pdfall)):
	if pdfall[i] == '\n':
		if pdfall[i-1] == '.':
			newall += pdfall[i]
		elif not pdfall[i+1].isdigit():
			newall += ' '
			count = count + 1
		else:
			newall += pdfall[i]
	else:
		newall += pdfall[i]
print(newall)

outfile = open(OUTFILE,'w')
outfile.write(newall)


print(count)

newlist = newall.splitlines()
print(len(newlist))


##google 번역

translator = Translator()
print(type(translator.translate(u'Hi Hello bro.',dest='ko')))

f = open("translate.txt","w")
ko = open("onlyko.txt","w")


for data in newlist:
	print(len(data))
	print(data)
	try:
		print("###")
		text = ""
		text = translator.translate(data,dest='ko').text
		print(text)
		print(type(text))
		print("&&&")
		f.write(data)
		f.write('\n')
		f.write(text)
		ko.write(text + '\n\n')
		print("((()))")
		f.write('\n\n')

	
	
	except Exception as ex:
		f.write(data)
		f.write('\n')
		f.write('Error %d' %len(data))
		ko.write('Error %d' %len(data))
		f.write('\n\n')
		print(u"번역 오류")
		print(ex)
	
'''
def translate(sl,tl,word):
        #from sl to tl
        data = {'sl':'ko','tl':'en','text': 'word'}
 
        language_code = {'한' : 'ko','영':'en','독':'de','일':'ja','아':'ar','중':'zh-CN','불':'fr','러':'ru',
        '라':'la','스':'es','이':'it'}
 
        data['sl']=language_code[sl]
        data['tl']=language_code[tl]
        data['text'] = word
 
        querystring = urllib.urlencode(data)
        request = urllib2.Request('http://www.translate.google.com' + '?' + querystring )
		
		
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')
        opener = urllib2.build_opener()
        feeddata = opener.open(request).read()
        #print feeddata
        soup = BeautifulSoup(feeddata)
        return soup.find('span', id="result_box").get_text()
'''

#print translate('영','한',"hi")
		
##papago 
'''
url="https://openapi.naver.com/v1/papago/n2mt?source=en&target=ko&text="
request_url = "https://openapi.naver.com/v1/papago/n2mt"
headers= {"X-Naver-Client-Id": "E3Qm4KfmUlFJjFRsCuTf", "X-Naver-Client-Secret":"Qbj4Gdlgi2"}
for text in newlist:
	params = {"source": "en", "target": "ko", "text": text}
	response = requests.post(request_url, headers=headers, data=params)
	result = response.json()
	time.sleep(0.1)
	print(result)
'''




'''
for text in pdflines:
	if text[-1] == '\n':
		print('line changed')
'''


#print(pdftext)
