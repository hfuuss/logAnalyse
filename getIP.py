#coding:utf-8
#ss
#python getIP.py Bdlog.txt
import re
from sys import argv

script, file_name = argv

def read_file(file_name):
	_fLog = open(file_name)
	_fLine = _fLog.readline()
	
	while _fLine:
		reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
		print 'ss'
		
		ip = reip.search(_fLine).group()#字符串ip
		#ip = reip.findall(_fLine)#列表ip
		print ip
		_fLine = _fLog.readline()
		ipstr = str(ip)
		out = open("Bdip.txt","a")
		out.write(ipstr+'\n')
	_fLog.close()
	
read_file(file_name)
