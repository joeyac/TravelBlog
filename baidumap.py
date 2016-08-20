# -*- coding: utf-8 -*-
from baidumapapi import baidu

ak = 'FCxGRrMqyxUsUdvXucO4d3C2jtl1EnKD'

Map = baidu.MapApi([ak])

# location = Map.location_api.get_location_by_address(u'百度大厦', u'北京')
#
# address = Map.location_api.get_address_by_location({'lng': 116.322987, 'lat': 39.983424})
#
# address = Map.location_api.get_formatted_address(u'北京市海淀区百度大厦')
#
# location = Map.location_api.get_location_by_address(u'天津')

T = Map.place_api.get_place_all(u'银行', u'北京')

# 通过IP地址获得粗略的地址信息 基本只能精确到市
# info = Map.ip_api.get_place_by_ip()
# 通过以下方式获取经纬度
# x = info['content']['point']['x']
# y = info['content']['point']['y']
x = '116.35004'
y = '39.99072'
# city = info['content']['address_detail']['city']
# province = info['content']['address_detail']['province']
# print(city)
# print(province)
# print(info)

# 通过经纬度获得地区详细信息
address = Map.location_api.get_address_by_location({'lng': x, 'lat': y})
print(address)
# 通过地区获得经纬度信息
# location = Map.location_api.get_location_by_address(u'河北')





