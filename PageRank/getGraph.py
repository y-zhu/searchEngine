#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

def getGraph(path):
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            getGraph(filepath)  
        
        elif os.path.isfile(filepath):                         # ������ļ�����ֱ���ж���չ��
            if os.path.splitext(filepath)[1] == '.html':
                f = open(filepath, 'r')                        # ��html�ļ����ҳ����ļ���ָ���url����
                filecontent = f.read()
                f.close() 
                str = 'D:\\study\\term6\\searchEngines\\experiments\\searchEngine\\news.tsinghua.edu.cn\\'
                null = ""
                filepath = filepath.replace(str,null)
                filepath = filepath.replace("\\","/")
                outfile.write(filepath+":")
                linkPattern = re.compile("<a.*?href=\"/(.+?)\".*?<\/a>")
                urls = linkPattern.findall(filecontent)                
                #urls=re.findall('<a.*?href=.*?<\/a>',filecontent)
                if len(urls):
                    outfile.write(urls[0])
                    for i in range(1,len(urls)):
                      outfile.write(","+urls[i])                  
                outfile.write("\n")

rootpath = os.path.abspath('.') 

outfile = open('graph.txt', 'a')                      
getGraph(rootpath)
outfile.close()  


               
 



                       
    
