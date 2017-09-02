# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:47:31 2017

@author: zhuimeng
"""

from urllib import request
import re,os,time
import multiprocessing
from multiprocessing import Pool

def get_response(url):
    response = request.urlopen(url)
    page = response.read().decode('utf-8')

def get_ann(page):
    #<a href="/news,831120,580741660.html" title="达海智能:第二届董事会第十六次会议决议公告" >达海智能:第二届董事会第十六次会议决议公告</a>
    pattern = re.compile('<span class="l3"><em class="hinfo">公告</em> <a href="(.*?)" title="(.*?)" >.*?</a>.*?<span class="l6">%s</span>'%date)
    ann = re.findall(pattern,page)
    return ann

def wrt(filepath,stockcode,ann):
    if (ann == []) :
        pass
    else :        
        fname = filepath + '\\' + stockcode + ".txt"
        f = open(fname,'w')
        for i in range(len(ann)):
            f.writelines(ann[i])
        f.close()

def get_urls():
    file = open('stocks.txt')
    urls = []
    
    while True :
        #读取股票代码
        stock_id = file.readline().replace('\n','')
        
        #判断是否已经读取完毕
        if stock_id == '' :
            return urls
        else :
            #创建对应股吧网页url
            urls.append("http://guba.eastmoney.com/list," + stock_id + ".html")

def m(url):
    print(0)
    stockcode = re.split(r'[,\.]',url)[3]
    page = get_response(url)
    ann = get_ann(page)
    wrt(filepath,stockcode,ann)
    return True


date = '07-19' #date是全局变量，其他函数会用到，如果写成 date = input("日期：")  就出问题
#创建一个文件夹存储当日的所有公告信息
filepath = 'E:\\stocks\\' + date
if not os.path.exists(filepath):
    os.makedirs(filepath)


if __name__ == '__main__':
    t1 = time.time()
    
    urls = get_urls()
    #print(11)
    pool = Pool()
    #print(12)
    try:
        pool.map(m,urls)
    except Exception as e:
        print(e)
    #print(1)
    pool.close()
    #print(2)
    pool.join()
    #print(3)
    t2 = time.time()
    t = t2 - t1
    print(t)
