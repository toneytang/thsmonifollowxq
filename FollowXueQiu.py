import requests as rq
import json
from bs4 import BeautifulSoup as bs
import winsound
import time


xq_url1 = "https://xueqiu.com/P/ZH010389"
xq_url = "http://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH010389&count=20&page=1"

my_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Connection': 'keep-alive',
    'Host': 'xueqiu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

xq_session = rq.Session()

history_time = 0

while(True):
    time.sleep(5)
    html = xq_session.get(xq_url1, headers = my_headers)

    print(html)

    pos_start = html.text.find('SNB.cubeInfo = ') + len('SNB.cubeInfo = ')
    pos_end = html.text.find('SNB.cubePieData') - 2
    date_value = html.text[pos_start:pos_end]
    dic = json.loads(str(date_value))
    
    if history_time == 0:
        print(history_time)
        history_time = dic['last_success_rebalancing']['updated_at']
        print(history_time)
        continue
    elif history_time != dic['last_success_rebalancing']['updated_at']:
        history_time = dic['last_success_rebalancing']['updated_at']
        print(history_time)
        break;
        

#print(dic['last_success_rebalancing']['updated_at'])

#print(date_value[2])
#print(date_value[3])
print("start")
for i in range(20):
    winsound.Beep(2222,600)
    winsound.Beep(1000,600)

