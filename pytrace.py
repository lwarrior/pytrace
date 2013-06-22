#!/bin/env python
#-*-coding:utf-8-*-

__author__ = "Liu Warrior"
__version__ = "0.1"
__date__ = "2013-06-22"
__license__ = "GPL"
__email__ = "lchangliang@gmail.com"

import os
import sys
import re

argv0 = sys.argv[0] #script name
argv1 = sys.argv[1] #argv1, str
argv2 = sys.argv[2] #filename

cmd_string = "grep " + argv1 + " " + argv2 + " > tmp.txt"
f = os.popen(cmd_string)
f.close()

ret_set = []
file_obj = open('tmp.txt')
for line in file_obj:
  value = re.match(r'\[\w+\s\d{2}\s\d+:\d+:\d+\]\s\w+\[(\d+)\].*', line)
	thread_id = value.group(1)
	ret_set.append(thread_id)
file_obj.close()

result = list(set(ret_set))
print "len:",len(result)
isfile=os.path.isfile("./list.txt")
if isfile:
	os.remove("./list.txt")
for item in result:
	cmd_str = "grep " + "\"\[" + item + "\]\"" + " " + argv2 + " >> list.txt"
	f = os.popen(cmd_str)
	f.close()
os.remove("./tmp.txt")
