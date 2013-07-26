#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# solved the problem \" Finding a Shared Motif \"
# Author: Jiahui Liu <beckyljh@gmail.com>,2013-07-25
# 思路：将每条序列切割，后取common，但耗时太长，亟需优化，见13_rosalind2.py

def allstr(str):
	alla = set()
	# range(0,3) 既表示0,1,2，而并没有3，所以此处不用len(str)-1
	for i in range(0,len(str)):
		for j in range(i+1,len(str)+1):
			# ruby中str[1,2]表示从第一个开始取长度为2的字符串，即“12”
			# python中str[1:2]表示取1前面空位到2前面空位之间的字符串，即“1”
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
	alldna.append(list(allstr(line[1])))

common = alldna[0]
for i in range(1,len(alldna)):
	common = set(alldna[i]) & set(common) 

longcommon = list(common)[0]
for i in range(1,len(common)):
	if len(list(common)[i]) >= len(longcommon):
		longcommon = list(common)[i]
	else:
		next
	
print longcommon

# 获取两个list的common元素
# a = [1,2]
# b = [2,3]
# c = set(a) & set(b)
# print list(c)
