from string import *
from os import getpid
from subprocess import check_output, STDOUT
import re

pid = getpid()

f = open('./trashme.txt', 'w')
f.write('This is a test\n')

lsof = (check_output(['/usr/sbin/lsof', '-p', str(pid)], stderr=STDOUT)).split("\n")
print lsof[0]
for line in lsof[1:]:
    if (re.search('trashme', line)): print line 

f.close

# COMMAND  PID USER   FD   TYPE     DEVICE  SIZE/OFF    NODE NAME
# python  6995 greg    3w   REG       14,2         0 2273252 /Users/greg/Desktop/trashme.txt