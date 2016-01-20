#coding:utf-8
#ss
#python getIP.py Bdlog.txt bdip.txt
#能够提取ip地址，并且可以去重
import re
from sys import argv

script, file_name, out_File = argv

def read_file(file_name):
	_fLog = open(file_name)
	_fLine = _fLog.readline()
	ips = []
	sep = '\n'
	while _fLine:
		reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
		#print 'ss'
		
		#ip = reip.search(_fLine).group()#字符串ip
		ip = reip.findall(_fLine)#列表ip
		#print ip
		if ip not in ips:
			ips.append(ip)
		_fLine = _fLog.readline()
	out = open(out_File,"a")
	for iptmp in ips:
		ipstr = str(iptmp)
		out.write(ipstr+sep)
	out.close()
	_fLog.close()
	print "the work done!"


read_file(file_name)
