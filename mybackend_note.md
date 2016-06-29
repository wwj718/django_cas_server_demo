# 任务
本地有一张可供远程同步的用户表，django以为为用户信息表。对外提供cas服务


# 自定义认证后端
cas 中存在一种需求，后端可能街道既有的数据库中或其他既有用户系统中，所以
如何写自定义认证后端就是一个问题

最灵活的方法就是直接手写认证后端

参考[在Django中自定义身份验证](http://python.usyiyi.cn/django/topics/auth/customizing.html)

# 思路
如readme里记的

*  采用django的Authenticate机制,写自己的认证后端
*  关注REMOTE_USER，主要使用单点登录解决方案


# 问题
直接改已有认证后端的问题，密码项目没法控制，或者说应当弄懂如何用python来操作这个django的用户数据库

才能使其可操作（对接到其他地方），任务就是理解它的原理

[Django中的密码管理](http://python.usyiyi.cn/django/topics/auth/passwords.html)

或者使用django的用户机制，但是修改验证的机制，这样可以绕开密码的问题

# 自定义后端（实施）
*  配置中的AUTHENTICATION_BACKENDS，Django 将在第一个匹配成功后停止处理
*  AUTH_USER_MODEL
*  定义一个django_app，在里边写新的用户表（models）和backend
    *  auth_backends,模仿edx项目起名 
    *  这是极简的demo：http://django.zone/blog/posts/custom-authentication-backends-django/
*  有时候会报错：user属性不够:诸如is_active，是其他部分依赖吗，中间件，那么认证后端怎么办，返回的user属性必须足够丰富啊，否则user不合格
    *  cas依赖那些属性
    *  需要继承user吗,继承后如何更改密码策略,自己实现密码检验？
# 意外收获
### 定制用户相关问题
*  https://docs.djangoproject.com/en/dev/topics/auth/customizing/
### 密码机制
*  http://tech.marksblogg.com/passwords-in-django.html


# 附
登录原理：认证是需要密码的，而是用户登录（逻辑上，给cookie）是不需要密码的，在认证确认后执行
