#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
1.此为GetData获取数据2.0版本代码。
2.新增功能：从某一时间开始，获取连续的n个数据包
'''

import os
import os.path
import re
import numpy as np
from scipy import io
import math

rootdir = r'E:\陈翔老师实验室\dataGSMR\20170117\1024\\'#指明数据存放的位置
rootdir = unicode(rootdir,"utf-8")

begin = 3600*6+60*38#相当于起始时间点
document_numble = 300#300个数据包，如果连续的话就是5分钟的频谱图

if __name__ == '__main__':
    for x1,x2,files in os.walk(rootdir):#files变量即所有文件
        pass

    file_count=0#数据文件总数

    for f in files[:]:
        if re.match(r'.*_F\.dat',f):#根据文件名，判断是否是所需的数据文件
            file_count=file_count+1
            if file_count>(document_numble+begin):#为了节省时间，后面的就不用再读取了
                break
        else:
            files.remove(f)#若不是数据文件则删除

    if file_count<document_numble:
        document_numble=file_count
    if file_count<document_numble+begin:
        document_numble=file_count
        begin=0
        
    data_matrix = np.zeros((document_numble,8192))#创建一个矩阵用于存储所有原始数据
    data_matrix_temp = np.zeros((document_numble,8192))#创建一个矩阵用于存储处理后的数据

    sample_files = files[begin:begin+document_numble]

    def process_Data(a):#对数据进行处理的函数
        if a==0:
            a=1
        return 20.0*math.log10(a)
    
    for i,f in enumerate(sample_files[:]):
        print '%.2f'%(float(i+1)*100/document_numble),'%'
        context = open(rootdir+f,'r').read() #读取一个文件
        open(rootdir+f,'r').close()#及时关闭文件
        search_result = re.search(r'"Data":.*\], "',context)#正则表达式寻找数据段
        data_temp1 = search_result.group()[9:-4]#忽略文字，提取数据
        data_temp2 = re.split(r'[\s\,]+',data_temp1)#将字符串形式的数据分割为list
        data = map(float,data_temp2)#将str类型的数据转换为float
            
        #以上，data存储了文件中读取的数据，数据提取结束
            
        data_matrix[i]=data#将当前文件中的数据添加入数据矩阵中
        data_matrix_temp[i]=map(process_Data,data)#20log10()


    data_matrix=np.transpose(data_matrix) #矩阵转置
    data_matrix_temp=np.transpose(data_matrix_temp) #矩阵转置
    Grddata=data_matrix_temp[788:1209]-133-30
    Grudata=data_matrix_temp[4884:5305]-135-30

    io.savemat(rootdir+'HSCData.mat', {'data': data_matrix})#保存文件，文件名千万
    io.savemat(rootdir+'qsdown.mat', {'Grddata': Grddata})#不能改！如果改的话一定
    io.savemat(rootdir+'qsup.mat', {'Grudata': Grudata})#要改Plot.py中的文件名！


    os.system("python Plot2.py")#执行画图程序，不用管


