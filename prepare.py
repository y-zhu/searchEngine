#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

def dirlist(path):
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath)  
        
        elif os.path.isfile(filepath):                         # 如果是文件，则直接判断扩展名
            if os.path.splitext(filepath)[1] == '.html':
                f = open(filepath, 'r')                        # 打开html文件，找出该文件中指向的url链接
                filecontent = f.read()
                f.close() 
                str = 'D:\\study\\term6\\searchEngines\\experiments\\searchEngine\\news.tsinghua.edu.cn\\'
                null = ""
                filepath = filepath.replace(str,null)
                outfile.write(filepath+":")
                linkPattern = re.compile("<a.*?href=\"/(.+?)\".*?<\/a>")
                urls = linkPattern.findall(filecontent)                
                #urls=re.findall('<a.*?href=.*?<\/a>',filecontent) 
                for i in urls:
                    if i[0:7]=="publish":
                        outfile.write(i+",")
                outfile.write("\n")
                

rootpath = os.path.abspath('.')                
outfile = open('prepare.txt', 'a')                      # 以追加方式打开输出文件
dirlist(rootpath)
outfile.close()                          
    
