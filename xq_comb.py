import requests as rq
import json
from bs4 import BeautifulSoup as bs
import winsound
import time

class XqComb():
    def __init__(self, combine_code):
        self.xq_url = "https://xueqiu.com/P/" + combine_code
        self.s = rq.Session()
        self.my_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'Connection': 'keep-alive',
        'Host': 'xueqiu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        } 
        self.history_time = 0
        #self.get_comb_status_change()
        
        
    def get_comb_status_change(self):
        html = self.s.get(self.xq_url, headers = self.my_headers)

        print(html)

        pos_start = html.text.find('SNB.cubeInfo = ') + len('SNB.cubeInfo = ')
        pos_end = html.text.find('SNB.cubePieData') - 2
        date_value = html.text[pos_start:pos_end]
        #print(date_value)
        dic = json.loads(str(date_value))
        self.last_operation = dic['sell_rebalancing']['rebalancing_histories'][0]
        if self.history_time == 0:
            print(self.history_time)
            self.history_time = dic['last_success_rebalancing']['updated_at']
            print(self.history_time)
            return True
        elif self.history_time != dic['last_success_rebalancing']['updated_at']:
            self.history_time = dic['last_success_rebalancing']['updated_at']
            print(self.history_time)
            return True



        

#print(dic['last_success_rebalancing']['updated_at'])

#print(date_value[2])
#print(date_value[3])
#print("start")
#for i in range(20):
#    winsound.Beep(2222,600)
#    winsound.Beep(1000,600)

