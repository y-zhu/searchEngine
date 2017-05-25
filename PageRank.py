# -*- coding: utf-8 -*-
import sys
import re

PR = {} #pagerankֵ
I = {} #�м����
indegree = {} #��¼��ҳ���
outdegree = {} #��¼��ҳ����
nodeName = {} #��¼��ҳ�ڵ��Ӧ����������
TN = 30 #��������������̶�Ϊ20��
a = 0.15 #����a������ȡ0.15
N = 0 #�ڵ���������������ļ����ͳ����ȷ�ڵ����
S = 0.0 #��¼�޳�����ҳ�ڵ��pagerankֵ֮��
x = [] #��ͼ����
y = []

#��ȡwiki.graph�ļ��õ�������ҳ������ӹ�ϵ
def read_wikiGraph():
    fopen = open("prepare.txt","r")
    for line in fopen:
        line = line.strip('\n')
        data = re.split('[:,]',line) #data[0]ΪԴ�ڵ㣬data[i](i > 0)Ϊdata[0]�ĳ��Ƚڵ�
        
        #��¼Դ�ڵ��outdegree
        if not outdegree.has_key(data[0]):
            outdegree[data[0]] = 0
        outdegree[data[0]] += len(data) - 1;
        #���ڳ��Ƚڵ㣬ͬ���������outdegree�ʵ�֮��
        for i in range(1,len(data)):
            if not outdegree.has_key(data[i]):
                outdegree[data[i]] = 0
        #��Դ�ڵ���뵽���Ƚڵ����Ƚڵ�ʵ��У�ͬʱԴ�ڵ����ʵ䣬�����Ϊ��
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
    #��ʼ��
    global S,N,a
    for i in outdegree.keys():
        PR[i] = 1.0 / N
        I[i] = a / N
        if outdegree[i] == 0:
            S = S + PR[i]
    #��������

    for k in range(1 , TN):
        #����I(j)
        for i in indegree.keys():
            temp = indegree[i]
            for j in range(0 , len(temp)):
                I[i] = I[i] + (1 - a) * PR[temp[j]] / outdegree[temp[j]]
        # ����PR(k)
        for n in PR:
            PR[n] = I[n] + (1.0 - a) * S / N
            I[n] = a / N
        # ����S(k + 1)
        S = 0
        for n in PR.keys():
            if outdegree[n] == 0:
                S = S + PR[n]

    ans = sorted(PR.iteritems() , key = lambda asd:asd[1] , reverse = True)
    
    # ����������ʽΪ��nodeName(nodeID):PageRank,outdegree,indegree
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
    
        
