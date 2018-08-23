#-*-coding=utf-8-*-

import pandas
from futuquant import *

class GetHoldChange(object):
    #获取高管持仓列表

    def __init__(self):
        pandas.set_option('display.width', 1000)
        pandas.set_option('max_columns', 1000)

    def test1(self):
        host = '127.0.0.1'
        port=11111
        quote_ctx = OpenQuoteContext(host,port)
        print(quote_ctx.get_holding_change_list(code='US.AAPL', holder_type=StockHolder.INSTITUTE, start_date='2017-01-01', end_date='2018-8-30'))

    def test2(self):
        host = '127.0.0.1'
        port = 11111
        quote_ctx = OpenQuoteContext(host, port)
        ret_code,ret_data = quote_ctx.get_holding_change_list(code='US.AAPL', holder_type=StockHolder.EXECUTIVE, start_date='2017-01-01', end_date='2018-8-30')
        holding_qty_list = ret_data['holding_qty']
        # holding_ratio_list = ret_data['holding_ratio']
        change_qty_list = ret_data['change_qty']
        change_ratio_list = ret_data['change_ratio']

        for i in range(len(ret_data)):
            change_ratio_temp = change_qty_list[i]/(holding_qty_list[i] - change_qty_list[i])
            change_ratio_temp = round(change_ratio_temp,4)
            if change_ratio_temp != change_ratio_list[i]:
                print('变动比例与预期不符！')
                print('change_ratio_temp = ', change_ratio_temp)
                print('change_ratio = ', change_ratio_list[i])




if __name__ == '__main__':

    ghc = GetHoldChange()
    ghc.test1()