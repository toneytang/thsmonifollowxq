from xq_comb import XqComb
from thstrader import THSTrader
import time
import winsound


xqcomb = XqComb("ZH010389")
ths_user = THSTrader()
ths_user.set_cookie('Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1532055934; user=MDp0ZXN0X3Rlc3QyMTo6Tm9uZTo1MDA6Mzk0MjkwNzI1OjcsMTExMTExMTExMTEsNDA7NDQsMTEsNDA7NiwxLDQwOzUsMSw0MDozOjo6Mzg0MjkwNzI1OjE1MzIwNTU5Mzc6OjoxNDg5NTQzMjYwOjYwNDgwMDowOjEyOWZiY2FhZmNlYTNhYzFmNTZmMGVkMDYzZGQwOGZkOTpkZWZhdWx0XzI6MA%3D%3D; userid=384290725; u_name=test_test21; escapename=test_test21; ticket=bd4a025a585b88b072d603b62f89c902; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1532055942; PHPSESSID=758ed26ecae08370372ad2e4781612e9; isSaveAccount=0')

#print(str(xqcomb.last_operation))

while(True):
    #每次循环休息3秒钟，防止被雪球网站屏蔽
    time.sleep(3)
    #给同花顺模拟平台一个心跳，保持连接
    ths_user.heartbeat()
    #每次查看组合是否有新的调仓动作，如果有，就进行相应操作
    if(xqcomb.get_comb_status_change()):
        #获取当前调仓目标股票号码
        operate_stock_code = xqcomb.last_operation["stock_symbol"][2:8]
        #获取当前调仓目标的成交价格
        operate_stock_price = xqcomb.last_operation["price"]
        #如果当前调仓后目标股票的权重大于50，说明是买入，否则说明是卖出
        if xqcomb.last_operation["weight"] > 50 :
            #计算可用余额
            kyye = ths_user.get_available_case()
            #因为有3秒延迟，所以提高买价4分钱，以防买不到，另外，不能提高太多，以免追高
            price = operate_stock_price+0.04
            #按照可用余额和下单价格计算出下单的数量，以100股为单位
            amount = ((kyye/price)/100) * 100
            #在模拟平台下买单指令
            ths_user.buy(operate_stock_code,price, amount)
        else:
            #查看是否持有该股，并返回可卖数量
            stock_available_sell = ths_user.get_position(operate_stock_code)
            #以低于调仓价格6分钱，抛出所有股票。因为有3秒延迟，所以调低6分钱，以防卖不出去。
            ths_user.sell(operate_stock_code,operate_stock_price-0.06, stock_available_sell)
        #报警信号，告知有操作发生
        for i in range(2):
            winsound.Beep(2222,600)
            winsound.Beep(1000,600)


    
