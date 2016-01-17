#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# author: hfuuss
# demo: python logAnalyse.py ex160113.log
# date:2016/1/17
# 本脚本是分析 网站基于iis服务器log分析脚本
#  功能：1、提取404页面url 
#        2、提取常用蜘蛛的url（10个）
import urllib
import re
from sys import argv

script, file_name = argv

#写入文件
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

		
#读取文件
def read_file(file_name):
	_fLog = open(file_name)
	_fLine = _fLog.readline()
	
	while _fLine:
		write_file(_fLine),
		_fLine = _fLog.readline()
	_fLog.close()
#蜘蛛整理
def FilterSpiderBD(log):
	pattern = re.compile(r'Baiduspider')#百度蜘蛛
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True

def FilterSpiderGG(log):
	pattern = re.compile(r'Googlebot')#谷歌蜘蛛
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True
def FilterSpider360(log):
	pattern = re.compile(r'360Spider')#360蜘蛛
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True
		
def FilterSpiderSS(log):
	pattern = re.compile(r'Sosospider')#soso蜘蛛
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True	

def FilterSpiderYH(log):
	pattern = re.compile(r'Yahoo!')#雅虎蜘蛛
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True	

def FilterSpiderYD(log):
	pattern = re.compile(r'YoudaoBot')#有道蜘蛛
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True		

def FilterSpiderSG(log):
	pattern = re.compile(r'Sogou')#搜狗蜘蛛
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True
		
def FilterSpiderMSN(log):
	pattern = re.compile(r'msnbot')#MSN蜘蛛
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True
		
def FilterSpiderBY(log):
	pattern = re.compile(r'bingbot ')#必应蜘蛛
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True

def FilterSpiderYS(log):
	pattern = re.compile(r'YisouSpider ')#宜搜蜘蛛
	nlog = str(log)
	matchBD = pattern.search(nlog)
	
	if matchBD:
		return True
#一行一行处理
def Filter404(log):
	pattern = re.compile(r'404')
	nlog = str(log)
	match = pattern.search(nlog)
	
	if match:
		print match.group() 
		return True
		
	
read_file(file_name)