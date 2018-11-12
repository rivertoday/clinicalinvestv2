# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class ClinicalProjects(models.Model):
    STATUS = (
        (u'计划中', u'计划中'),
        (u'进行中', u'进行中'),
        (u'分析中', u'分析中'),
        (u'已结束', u'已结束'),
        (u'其他', u'其他'),
    )
    name = models.CharField(u'项目名称', max_length=100)
    prj_code = models.CharField(u'项目内部代号', max_length=100, default=u'testing')
    status = models.CharField(u'项目状态',max_length=10, choices=STATUS)
    starttime = models.DateField(u'开始日期',max_length=12)
    endtime = models.DateField(u'结束日期',max_length=12)
    linkurl = models.CharField(u'项目地址',max_length=50,default='#')
    description = models.TextField(u'项目介绍')

    class Meta:
        verbose_name = u'流调项目'
        ordering = ('id', 'name')