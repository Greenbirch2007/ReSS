#! coding:utf-8 -*-
import time
import os
from selenium import webdriver

import pymysql
import requests
import re
import urllib
from requests.exceptions import RequestException
from lxml import etree




def parse_co(html):
    big_list = []
    selector = etree.HTML(html)
    title = selector.xpath("/html/body/div[1]/div[2]/div[1]/div[3]/ul/li/div[1]/div/a/text()")
    link = selector.xpath("/html/body/div[1]/div[2]/div[1]/div[3]/ul/li/div[1]/div/a/@href")
    for i1,i2 in zip(title,link):
        big_list.append((i1,'https://www.nowcoder.com/'+i2))
    return big_list


def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='softStone',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,508):
        sql = 'select link from nkw_python where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        url = data['link']
        yield url



if __name__ =="__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)

    for url_str in Python_sel_Mysql():
        driver.get(url_str)
        html = driver.page_source
        time.sleep(3)




# salary,type,link,job_name
# create table nkw_python(
# id int not null primary key auto_increment,
# title text,
# link text
# ) engine=InnoDB  charset=utf8;

# drop table nkw_python;

#