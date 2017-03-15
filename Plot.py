#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
本版本绘图与1.0版本完全一样
'''
from scipy import io
import numpy as np
from matplotlib import pyplot as plt
import matplotlib  
import matplotlib.cm as cm 
from GetData2 import rootdir
#from pylab import *

#rootdir = r'E:\陈翔老师实验室\dataGSMR\20170108\1024\\'#指明数据存放的位置
#rootdir = unicode(rootdir,"utf-8")
#file_name = r'qsup.mat'

context = io.loadmat(rootdir+'qsup.mat')         #读取mat文件
Grudata = context['Grudata']            #获取数据
context = io.loadmat(rootdir+'qsdown.mat')         #读取mat文件
Grddata = context['Grddata']            #获取数据

(c,r) = Grudata.shape    #size

t = np.linspace(1,r,r)
fu = np.linspace(885,889,421)
fd = np.linspace(930,934,421)

[T,Fu] = np.meshgrid(t,fu)
[T,Fd] = np.meshgrid(t,fd)
Zu = Grudata
Zd = Grddata

vmin=min(Grudata.min(),Grddata.min())
vmax=max(Grudata.max(),Grddata.max())
norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax) #归一化colorbar
fig = plt.figure(figsize=(10,8), dpi=80, facecolor="white")

ax = fig.add_subplot(121) 
plt.pcolormesh(T, Fu, Zu,norm=norm,cmap = matplotlib.cm.jet)#pcolor比pcolor快很多
ax.set_xlabel('Time/s')
ax.set_ylabel('Frequency/MHz')
plt.title('Uplink')
ax = fig.add_subplot(122)
plt.pcolormesh(T, Fd, Zd,norm=norm,cmap = matplotlib.cm.jet)
ax.set_xlabel('Time/s')
ax.set_ylabel('Frequency/MHz')
plt.title('Downlink')

cbar = plt.colorbar()#使用颜色条
cbar.set_ticks(np.linspace(vmin,vmax,8))
cbar.set_label('Amplitude/dBm')
plt.show()

'''
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10,8), dpi=80, facecolor="white")
ax = Axes3D(fig)
plt.title('Uplink')
ax.set_xlabel('Time/s')
ax.set_ylabel('Frequency/MHz')
ax.set_zlabel('Amplitude/dBm')
ax.plot_surface(T, Fu, Zu, rstride=1, cstride=1, cmap='rainbow')
#plt.show()
fig = plt.figure(figsize=(10,8), dpi=80, facecolor="white")
ax = Axes3D(fig)
ax.set_xlabel('Time/s')
ax.set_ylabel('Frequency/MHz')
ax.set_zlabel('Amplitude/dBm')
plt.title('Downlink')
ax.plot_surface(T, Fd, Zd, rstride=1, cstride=1, cmap='rainbow')
plt.show()
'''
