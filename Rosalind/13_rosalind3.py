#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# solved the problem \" Finding a Shared Motif \"
# Author: Jiahui Liu <beckyljh@gmail.com>,2013-07-26
# 思路：针对数组删除元素时间过长，先采用字典存储子序列
# 将第一条序列切割，存入字典，后判断数组内每段子序列是否存在于之后的每段数列中，
# 存在则保存子序列，否则从字典内删除子序列

from copy import deepcopy

def allstr(str):
	dic = {}
	for i in range(0,len(str)):
		for j in range(i+1,len(str)+1):
			dic[str[i:j]] = str[i:j]
	return dic

alldna = {}
file = open("rosalind_lcsm.txt")
input = file.read()
each = input.split(">")
for i in range(0,len(each)):
	line = each[i].split("\r\n")
	for i in range(2,len(line)):
		line[1] = line[1] + line[i]

	alldna = allstr(line[1])
	break

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

	for (k,v) in alldna.items():
		if (k not in line[1]) and (k in allb):
			del allb[k]

# 字典按元素长度排序
ll = sorted(allb,key=len)
print ll[-1]
