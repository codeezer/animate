#!/usr/bin/env python
# -*- coding:utf-8 -*-
import animate
import threading
import time

def write2file(x,y):
    f = open("sampleText.txt","a")
    f.write(str(x)+','+str(y)+'\n')
    f.close()

for i in range(10,500):

    write2file(i,i/3-i*i)
    time.sleep(0.01)
