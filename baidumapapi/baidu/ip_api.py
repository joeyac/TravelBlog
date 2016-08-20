# -*- coding: utf-8 -*-
# __author__ = 'crazyX'

import requests
import json
import logging

logger = logging.getLogger('mapapi')


class IpApi(object):
    ip_url = 'http://api.map.baidu.com/location/ip'
    # 返回结果（地址解析的结果）
    # {
    #     address: "CN|北京|北京|None|CHINANET|1|None",  # 地址
    #     content:  # 详细内容
    #         {
    #             address: "北京市",  # 简要地址
    #             address_detail:  # 详细地址信息
    #                 {
    #                     city: "北京市",  # 城市
    #                     city_code: 131,  # 百度城市代码
    #                     district: "",  # 区县
    #                     province: "北京市",  # 省份
    #                     street: "",  # 街道
    #                     street_number: ""  # 门址
    #                 },
    #             point:  # 百度经纬度坐标值
    #                 {
    #                     x: "116.39564504",
    #                     y: "39.92998578"
    #                 }
    #         },
    #     status: 0  # 返回状态码

    def __init__(self, scheduler):
        self.scheduler = scheduler

    def get_place_by_ip(self, ip='', coor='bd09ll'):

        params = {'ip': ip, 'coor': coor, 'ak': self.scheduler.next()}
        r = requests.get(self.ip_url, params=params)
        try:
            r.raise_for_status()
            data = json.loads(r.text)
            # print json.dumps(data, ensure_ascii=False)
            if data['status'] == 0:
                return data
            else:
                logger.debug('failed to get place by ip, return result is %s' % r.text)
                return None
        except Exception as e:
            pass
        return None