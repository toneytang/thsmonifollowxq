# coding: utf-8
from __future__ import division, unicode_literals

import math
import logging
import os
import random
import re
from bs4 import BeautifulSoup as bs
import json

import requests





class THSTrader():
    def __init__(self, debug=True):
        self.cookie = None
        self.account_config = None
        self.s = requests.Session()
        self.exchange_stock_account = dict()
		#self.position = [[]]
    def set_cookie(self, my_cookie):
        my_headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Cookie':my_cookie,
            'Host':'mncg.10jqka.com.cn',
            'Referer':'http://moni.10jqka.com.cn/',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        self.s.headers.update(my_headers)

    def heartbeat(self):
        hb_url = 'http://mncg.10jqka.com.cn/cgiwt/index/index'
        res = self.s.get(hb_url)
        #print self.s.headers
        print (res.status_code)
    def buy(self, stock_code, price, amount=0, volume=0, entrust_prop='limit'):
        """买入股票
        :param stock_code: 股票代码
        :param price: 买入价格
        :param amount: 买入股数
        :param volume: 买入总金额 由 volume / price 取整， 若指定 price 则此参数无效
        :param entrust_prop: 委托类型 'limit' 限价单 , 'market'　市价单
        """
        stock_code = str(stock_code)
        price = str(price)
        amount = str(amount)
        if stock_code.startswith(('50', '51', '60', '73', '90', '110', '113', '132', '204', '78')):
            mkcode = '2'
            gdzh = 'A472194268'
        if stock_code.startswith(('00', '13', '18', '15', '16', '18', '20', '30', '39', '115', '1318')):
            mkcode = '1'
            gdzh = '0096474145'

        url = 'http://mncg.10jqka.com.cn/cgiwt/delegate/tradestock/'
        my_data = {
            "type":"cmd_wt_mairu",
            "mkcode":mkcode,
            "gdzh":gdzh,
            "stockcode":stock_code,
            "price":price,
            "amount":amount
        }
        #print(my_data)
        r = self.s.post(url, data=my_data)
        #print(r.content)
        #print self.s.headers
        #print(r.url)
        print ("buy" + str(r.status_code))
        #print r.content
		
		
    def sell(self, stock_code, price, amount=0, volume=0, entrust_prop='limit'):
        """卖出股票
        :param stock_code: 股票代码
        :param price: 卖出价格
        :param amount: 卖出股数
        :param volume: 卖出总金额 由 volume / price 取整， 若指定 amount 则此参数无效
        :param entrust_prop: str 委托类型 'limit' 限价单 , 'market'　市价单
        """
        stock_code = str(stock_code)
        price = str(price)
        amount = str(amount)
        if stock_code.startswith(('50', '51', '60', '73', '90', '110', '113', '132', '204', '78')):
            mkcode = '2'
            gdzh = 'A472194268'
        if stock_code.startswith(('00', '13', '18', '15', '16', '18', '20', '30', '39', '115', '1318')):
            mkcode = '1'
            gdzh = '0096474145'

        url = 'http://mncg.10jqka.com.cn/cgiwt/delegate/tradestock'
        my_data = {
            'type':'cmd_wt_maichu',
            'mkcode':mkcode,
            'gdzh':gdzh,
            'stockcode':stock_code,
            'price':price,
            'amount':amount
        }
        r = self.s.post(url, data = my_data)
        print ("sell" + str(r.status_code))
		
    def get_position(self, stock_num):
        #获取持仓股票
        url = 'http://mncg.10jqka.com.cn/cgiwt/delegate/qryChicang'
        r = self.s.get(url)
        dic = json.loads(r.text)
        for stock in dic["result"]["list"] :
            if stock['d_2102'] == stock_num :
                return stock['d_2121']
        return 0
        #print(r.content)
        #print(dic["result"]["list"][0]["d_2102"])
        
    def get_available_case(self):
        #获取当前可用资金
        url = 'http://mncg.10jqka.com.cn/cgiwt/query/querydiv/?ajaxdatatype=html'
        r = self.s.get(url)
        soup = bs(r.content, "html.parser")
        #print(soup)
        kyye = float(soup.findAll('td', id = "kyye")[0].string)
        print(kyye)
        return kyye
        

'''
ths_user = THSTrader()
ths_user.set_cookie('Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1532055934; user=MDp0ZXN0X3Rlc3QyMTo6Tm9uZTo1MDA6Mzk0MjkwNzI1OjcsMTExMTExMTExMTEsNDA7NDQsMTEsNDA7NiwxLDQwOzUsMSw0MDozOjo6Mzg0MjkwNzI1OjE1MzIwNTU5Mzc6OjoxNDg5NTQzMjYwOjYwNDgwMDowOjEyOWZiY2FhZmNlYTNhYzFmNTZmMGVkMDYzZGQwOGZkOTpkZWZhdWx0XzI6MA%3D%3D; userid=384290725; u_name=test_test21; escapename=test_test21; ticket=bd4a025a585b88b072d603b62f89c902; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1532055942; PHPSESSID=758ed26ecae08370372ad2e4781612e9; isSaveAccount=0')
stock_available_sell = ths_user.get_position('002807')
print(stock_available_sell)
stock_available_sell = ths_user.get_position('600022')
print(stock_available_sell)
stock_available_sell = ths_user.get_position('600023')
print(stock_available_sell)
'''
