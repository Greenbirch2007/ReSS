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


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='softStone',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into nkw_python (title,link) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass

if __name__ =="__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)


    for url_n in range(1,27):
        url = 'https://www.nowcoder.com/search?type=question&order=hot&query=python&subType={0}'.format(url_n)
        driver.get(url)
        html = driver.page_source
        content =parse_co(html)
        insertDB(content)




# salary,type,link,job_name
# create table nkw_python(
# id int not null primary key auto_increment,
# title text,
# link text
# ) engine=InnoDB  charset=utf8;

# drop table nkw_python;

#