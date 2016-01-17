#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# author: hfuuss
# demo: python logAnalyse.py ex160113.log
# date:2016/1/17
# ���ű��Ƿ��� ��վ����iis������log�����ű�
#  ���ܣ�1����ȡ404ҳ��url 
#        2����ȡ����֩���url��10����
import urllib
import re
from sys import argv

script, file_name = argv

#д���ļ�
def write_file(line):
	
	if Filter404(line): 
		_nlog = open("404log.txt","a")
		_nlog.write(line)
		_nlog.close()
	
	if FilterSpiderBD(line): 
		_BdLog = open("BdLog.txt","a")
		_BdLog.write(line)
		_BdLog.close()
	
	if FilterSpiderGG(line): 
		_BdLog = open("GGLog.txt","a")
		_BdLog.write(line)
		_BdLog.close()
		
	if FilterSpider360(line): 
		_BdLog = open("360Log.txt","a")
		_BdLog.write(line)
		_BdLog.close()
		
	if FilterSpiderSS(line): 
		_BdLog = open("SSLog.txt","a")
		_BdLog.write(line)
		_BdLog.close()	
	
	if FilterSpiderYH(line): 
		_BdLog = open("YHLog.txt","a")
		_BdLog.write(line)
		_BdLog.close()
		
	if FilterSpiderYD(line): 
		_BdLog = open("YDLog.txt","a")
		_BdLog.write(line)
		_BdLog.close()
	
	if FilterSpiderSG(line): 
		_BdLog = open("SGLog.txt","a")
		_BdLog.write(line)
		_BdLog.close()
		
	if FilterSpiderMSN(line): 
		_BdLog = open("MSNLog.txt","a")
		_BdLog.write(line)
		_BdLog.close()

	if FilterSpiderBY(line): 
		_BdLog = open("BYLog.txt","a")
		_BdLog.write(line)
		_BdLog.close()
	
	if FilterSpiderYS(line): 
		_BdLog = open("YSLog.txt","a")
		_BdLog.write(line)
		_BdLog.close()

		
#��ȡ�ļ�
def read_file(file_name):
	_fLog = open(file_name)
	_fLine = _fLog.readline()
	
	while _fLine:
		write_file(_fLine),
		_fLine = _fLog.readline()
	_fLog.close()
#֩������
def FilterSpiderBD(log):
	pattern = re.compile(r'Baiduspider')#�ٶ�֩��
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True

def FilterSpiderGG(log):
	pattern = re.compile(r'Googlebot')#�ȸ�֩��
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True
def FilterSpider360(log):
	pattern = re.compile(r'360Spider')#360֩��
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True
		
def FilterSpiderSS(log):
	pattern = re.compile(r'Sosospider')#soso֩��
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True	

def FilterSpiderYH(log):
	pattern = re.compile(r'Yahoo!')#�Ż�֩��
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True	

def FilterSpiderYD(log):
	pattern = re.compile(r'YoudaoBot')#�е�֩��
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True		

def FilterSpiderSG(log):
	pattern = re.compile(r'Sogou')#�ѹ�֩��
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True
		
def FilterSpiderMSN(log):
	pattern = re.compile(r'msnbot')#MSN֩��
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True
		
def FilterSpiderBY(log):
	pattern = re.compile(r'bingbot ')#��Ӧ֩��
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True

def FilterSpiderYS(log):
	pattern = re.compile(r'YisouSpider ')#����֩��
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True
#һ��һ�д���
def Filter404(log):
	pattern = re.compile(r'404')
	nlog = str(log)
	match = pattern.search(nlog)
	
	if match:
		print match.group() 
		return True
		
	
read_file(file_name)