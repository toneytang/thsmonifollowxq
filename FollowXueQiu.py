from xq_comb import XqComb
from thstrader import THSTrader
import time


xqcomb = XqComb("ZH010389")
ths_user = THSTrader()
ths_user.set_cookie('Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1532055934; user=MDp0ZXN0X3Rlc3QyMTo6Tm9uZTo1MDA6Mzk0MjkwNzI1OjcsMTExMTExMTExMTEsNDA7NDQsMTEsNDA7NiwxLDQwOzUsMSw0MDozOjo6Mzg0MjkwNzI1OjE1MzIwNTU5Mzc6OjoxNDg5NTQzMjYwOjYwNDgwMDowOjEyOWZiY2FhZmNlYTNhYzFmNTZmMGVkMDYzZGQwOGZkOTpkZWZhdWx0XzI6MA%3D%3D; userid=384290725; u_name=test_test21; escapename=test_test21; ticket=bd4a025a585b88b072d603b62f89c902; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1532055942; PHPSESSID=758ed26ecae08370372ad2e4781612e9; isSaveAccount=0')

#print(str(xqcomb.last_operation))

while(True):
    time.sleep(3)
    ths_user.heartbeat()
    if(xqcomb.get_comb_status_change()):
        operate_stock_code = xqcomb.last_operation["stock_symbol"][2:8]
        operate_stock_price = xqcomb.last_operation["price"]
        if xqcomb.last_operation["weight"] > 50 :
            ths_user.buy(operate_stock_code,operate_stock_price+0.04, 200)
        else:
            ths_user.sell(operate_stock_code,operate_stock_price-0.04, 200)

    
