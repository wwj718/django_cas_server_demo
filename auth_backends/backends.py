#!/usr/bin/env python
# encoding: utf-8
"""Django authentication backends.
For more information visit https://docs.djangoproject.com/en/dev/topics/auth/customizing/.
"""
#from django.conf import settings
#from django.contrib.auth.models import User, check_password
from auth_backends.models import  SeuUser

class SeuBackend(object):
    '''
    from django.contrib.auth import authenticate
    lyx = authenticate(username='lyx', password='master')
    if lyx: #验证非空，需要看下django-mama-cas中怎么做
        xxx

    dir(user) or user.[tab] 列出所有属性,要少于user wwj的属性
    user.backend #u'auth_backends.backends.SeuBackend'

    wwj = authenticate(username='wwj', password='wwj')
    #u'django.contrib.auth.backends.ModelBackend'
    '''
    def authenticate(self, username=None, password=None):
        try:
            user = SeuUser.objects.get(username=username)
            return user

            if password == 'master':
            #if password == user.password:
                # check password from user.password
                # Authentication success by returning the user
                return user
            else:
                # Authentication fails if None is returned
                return None
        except SeuUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return SeuUser.objects.get(pk=user_id)
        except SeuUser.DoesNotExist:
            return None
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name, and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'sha1$4e987$afbcf42e21bd417fb71db8c66b321e9fc33051de' ,如何产生

    @property
    def user_model(self):
        return SeuUser

    def authenticate(self, username=None, password=None):
        try:
            user = self.user_model.objects.get(username=username)
            if user.check_password(password): # 取决于存储的password是什么，而修改check_password函数
                return user
        except self.user_model.DoesNotExist:
            pass
        return None




    def get_user(self, user_id):
        try:
            return self.user_model.objects.get(pk=user_id)
        except self.user_model.DoesNotExist:
            return None
    """
