# coding=utf-8
from django.db import models

# Create your models here.


class Station(models.Model):
    # 标题
    title = models.CharField('标题', max_length=50)
    # 子标题
    sub_title = models.CharField('子标题', max_length=200, default='')
    # 简介
    intro = models.TextField('简介', default='')

    # 创建时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    # 最后更新时间
    last_update_time = models.DateTimeField('最后更新时间', blank=True, null=True, auto_now=True)

    # 到达时间
    arrival_time = models.DateTimeField('到达时间', blank=True, null=True, )
    # 离开时间
    leave_time = models.DateTimeField('离开时间', blank=True, null=True, )

    # 现在的位置 # place
    province = models.CharField('省份', max_length=50)
    city = models.CharField('城市', max_length=50)
    detail = models.CharField('详细信息', max_length=400, default='', blank=True, null=True, )
    lat = models.CharField('纬度', max_length=50, default='', blank=True, null=True, )
    lon = models.CharField('经度', max_length=50, default='', blank=True, null=True, )

    # 是否可见 不可见等于删除
    visible = models.BooleanField('是否可见', default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "station"
        ordering = ['-arrival_time']


class Event(models.Model):
    # 标题
    title = models.CharField('标题', max_length=50)
    # 描述
    description = models.TextField('描述', default='')

    # 创建时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    # 最后更新时间
    last_update_time = models.DateTimeField('最后更新时间', blank=True, null=True, auto_now=True)

    # 开始时间
    start_time = models.DateTimeField('开始时间', blank=True, null=True, )
    # 结束时间
    end_time = models.DateTimeField('结束时间', blank=True, null=True, )

    # 详细地址
    place_detail = models.CharField('地址详细信息', max_length=400, default='', blank=True, null=True, )
    lat = models.CharField('纬度', max_length=50, default='', blank=True, null=True, )
    lon = models.CharField('经度', max_length=50, default='', blank=True, null=True, )

    @property
    def location(self):
        if self.lat or self.lon:
            return "  lat: "+str(self.lat)+"  lon: "+str(self.lon)
        return None

    # 从属站点
    station = models.ForeignKey(Station, blank=True)

    # 是否可见 不可见等于删除
    visible = models.BooleanField('是否可见', default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "event"
        ordering = ['start_time']
