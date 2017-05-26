#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getPageName(path):
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            getPageName(filepath)  
        
        elif os.path.isfile(filepath):                         # 如果是文件，则直接判断扩展名
            if os.path.splitext(filepath)[1] == '.html':
                f = open(filepath, 'r')                        # 打开html文件，找出文件中的title
                filecontent = f.read()
                f.close() 
                str = 'D:\\study\\term6\\searchEngines\\experiments\\searchEngine\\news.tsinghua.edu.cn\\'
                null = ""
                filepath = filepath.replace(str,null)
                filepath = filepath.replace("\\","/")
                
		filecontent.decode('utf-8','ignore').encode('gbk','ignore')

                expression = '<title>(.*?)</title>'
                pattern = re.compile(expression)
                title = pattern.findall(filecontent)
		if len(title): 
			out.write(title[0].decode('utf-8','ignore').encode('gbk','ignore'))
                out.write("-->"+filepath+"\n")
                
rootpath = os.path.abspath('.') 

out = open("pageName.txt",'a')
getPageName(rootpath)
out.close()