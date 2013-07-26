#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# solved the problem \" Finding a Shared Motif \"
# Author: Jiahui Liu <beckyljh@gmail.com>,2013-07-25
# 思路：将第一条序列切割，存入数组，后判断数组内每段子序列是否存在于之后的每段数列中，
# 存在则保存子序列，其中数组删除元素花费时间过长，亟需优化，见13_rosalind3.py

from copy import deepcopy

def allstr(str):
	alla = set()
	for i in range(0,len(str)):
		for j in range(i+1,len(str)+1):
			alla.add(str[i:j])
	return alla

alldna = list()
file = open("rosalind_lcsm.txt")
input = file.read()
each = input.split(">")
for i in range(0,len(each)):
	line = each[i].split("\r\n")

	for i in range(2,len(line)):
		line[1] = line[1] + line[i]

	alldna = list(allstr(line[1]))
	break

# 或者用allb = alldna[:]都可以，就是不能用allb = alldna，这样只是引用，改变allb的同时会改变alldna
allb = deepcopy(alldna)
file = open("rosalind_lcsm.txt")
input = file.read()
each = input.split(">")
for i in range(0,len(each)):
	line = each[i].split("\r\n")
	c = len(allb)
	alldna = deepcopy(allb)
	# print c
	for i in range(2,len(line)):
		line[1] = line[1] + line[i]

	for i in range(0,c):
		if (alldna[i] not in line[1]) and (str(alldna[i]) in allb):
			# remove花费时间太长，亟需优化，见13_rosalind3.py
			allb.remove(str(alldna[i]))

# 数组按元素长度排序
allb.sort(key=len)
print allb[-1]
