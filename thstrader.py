# coding: utf-8
from __future__ import division, unicode_literals

import math
import logging
import os
import random
import re

import requests





class THSTrader():
    def __init__(self, debug=True):
        self.cookie = None
        self.account_config = None
        self.s = requests.Session()
        self.exchange_stock_account = dict()
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
            gdzh = 'A445281742'
        if stock_code.startswith(('00', '13', '18', '15', '16', '18', '20', '30', '39', '115', '1318')):
            mkcode = '1'
            gdzh = '0069561619'

        url = 'http://mncg.10jqka.com.cn/cgiwt/delegate/tradestock'
        my_data = {
            'type':'cmd_wt_mairu',
            'mkcode':mkcode,
            'gdzh':gdzh,
            'stockcode':stock_code,
            'price':price,
            'amount':amount
        }
        r = self.s.post(url, data = my_data)
        #print self.s.headers
        #print r.status_code
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
            gdzh = 'A445281742'
        if stock_code.startswith(('00', '13', '18', '15', '16', '18', '20', '30', '39', '115', '1318')):
            mkcode = '1'
            gdzh = '0069561619'

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
