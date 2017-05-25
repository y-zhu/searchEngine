# -*- coding: utf-8 -*-
import sys
import re

PR = {} #pagerank值
I = {} #中间变量
indegree = {} #记录网页入度
outdegree = {} #记录网页出度
nodeName = {} #记录网页节点对应的中文名称
TN = 30 #迭代次数，这里固定为20次
a = 0.15 #概率a，这里取0.15
N = 0 #节点个数，读入数据文件后可统计正确节点个数
S = 0.0 #记录无出度网页节点的pagerank值之和
x = [] #绘图坐标
y = []

#读取wiki.graph文件得到各个网页间的链接关系
def read_wikiGraph():
    fopen = open("prepare.txt","r")
    for line in fopen:
        line = line.strip('\n')
        data = re.split('[:,]',line) #data[0]为源节点，data[i](i > 0)为data[0]的出度节点
        
        #记录源节点的outdegree
        if not outdegree.has_key(data[0]):
            outdegree[data[0]] = 0
        outdegree[data[0]] += len(data) - 1;
        #对于出度节点，同样将其加入outdegree词典之中
        for i in range(1,len(data)):
            if not outdegree.has_key(data[i]):
                outdegree[data[i]] = 0
        #将源节点加入到出度节点的入度节点词典中，同时源节点加入词典，入度设为零
        if not indegree.has_key(data[0]):
            indegree[data[0]] = []
        for i in range(1,len(data)):
            if not indegree.has_key(data[i]):
                indegree[data[i]] = []
            indegree[data[i]].append(data[0])
    fopen.close()
    global N
    N = len(outdegree)    

def pageRank():
    #初始化
    global S,N,a
    for i in outdegree.keys():
        PR[i] = 1.0 / N
        I[i] = a / N
        if outdegree[i] == 0:
            S = S + PR[i]
    #迭代计算

    for k in range(1 , TN):
        #计算I(j)
        for i in indegree.keys():
            temp = indegree[i]
            for j in range(0 , len(temp)):
                I[i] = I[i] + (1 - a) * PR[temp[j]] / outdegree[temp[j]]
        # 计算PR(k)
        for n in PR:
            PR[n] = I[n] + (1.0 - a) * S / N
            I[n] = a / N
        # 计算S(k + 1)
        S = 0
        for n in PR.keys():
            if outdegree[n] == 0:
                S = S + PR[n]

    ans = sorted(PR.iteritems() , key = lambda asd:asd[1] , reverse = True)
    
    # 输出结果，格式为：nodeName(nodeID):PageRank,outdegree,indegree
    fout = open("result.txt","w")
    sum = 0
    for i in range(0 , len(ans)):
        sum += PR[ans[i][0]]
        fout.write(str(ans[i][0])+ ": " + str(PR[ans[i][0]]) + " , " + str(outdegree[ans[i][0]]) + " , " + str(len(indegree[ans[i][0]])) +"\n")
    fout.close()
    print sum
    

if __name__ == '__main__':
    read_wikiGraph()
    pageRank()
    
        
