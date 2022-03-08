from urllib import request
import re
import time
import random
import csv
from ua_info import ua_list
# 定义一个爬虫类
class MaoyanSpider(object): 
    # 初始化
    # 定义初始页面url
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start={}&filter='
    
    # 请求函数
    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)
    
    # 解析函数
    def parse_html(self,html):
		# 生成正则表达式对象
        pattern = re.compile(r'<span class="title">(.*?)</span>.*?<p class="">(.*?)<br>(.*?)</p>',re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)
    # 保存数据函数，使用python内置csv模块
    def save_html(self,r_list):
        #生成文件对象  
        with open('douban.csv','a',newline='',encoding="utf-16") as f:
            #生成csv操作对象
            writer = csv.writer(f)
            #整理数据
            for r in r_list:
            	name = r[0].strip()
            	star = r[1].strip()
            	time = r[2].strip()
            	L = [name, star, time]
            	writer.writerow(L)
                
    # 主函数
    def run(self):
    	begin = int(input("请输入起始页："))
    	end = int(input("请输入终止页："))
    	for start in range(25*(begin-1), 25*end, 25):
            url = self.url.format(start)
            self.get_html(url)
            #生成1-2之间的浮点数
            time.sleep(random.uniform(1,2))
# 以脚本方式启动
if __name__ == '__main__':
    #捕捉异常错误
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print("错误:",e)