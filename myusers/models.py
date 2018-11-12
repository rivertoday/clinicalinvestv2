# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.conf import settings
from django.contrib.auth import authenticate

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, user_name, phone, password=None):
        """
        Creates and saves a User with the given email, and password.
        """
        if not email:
            raise ValueError(u'用户需要以电子邮箱来创建！')

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            phone=phone,
        )
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, phone, password):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(email,
                                user_name=user_name,
                                phone=phone,
                                password=password
                                )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    # 修改密码
    def db_change_password(loginEmail, oldPassword, newPassword):
        user = authenticate(email=loginEmail, password=oldPassword)
        if user is not None:
            if user.is_active:
                user.set_password(newPassword)
                user.save()
                return 1  # 修改成功，允许特殊符号
            else:
                return -2  # 没有权限
        else:
            return -1  # 旧密码错误

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=u'电子邮箱',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(
        verbose_name=u'手机号',
        max_length=20,
        unique=True,
    )
    user_name = models.CharField(u'姓名', max_length=50, default='')
    hospital = models.CharField(u'所在单位', max_length=100, blank=True)
    address = models.CharField(u'单位地址', max_length=100, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'phone']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        # return self.is_admin
        return True #This setting is for debug

    class Meta:
        verbose_name = u'用户信息'
        permissions = (
            ("user_operation", "user_all_permissions"),
        )