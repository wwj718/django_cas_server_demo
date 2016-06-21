# cas_test
基于django的cas server

# Why
*  不想折腾java/tomcat/apache(apereo/cas)
*  利用django的认证机制易于与任何认证系统对接，包括数据库，以及jwt等
*  跟Open edX采用同一套技术栈
*  默认不采用https,方便开发，需要的话，采用nginx反向代理
*  why not

# Usage
把当前项目run起来后，访问`/django_cas/login`即可

# 运行效果图
![cas server](http://7xrc4h.com1.z0.glb.clouddn.com/cas.jpg)

# LICENSE
MIT


#  Setting Up Your Users

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

# Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html


# 项目创建
采用[cookiecutter-django](https://github.com/pydanny/cookiecutter-django)

禁用了大多特性，为了开发方便，数据库采用了sqlite

# 核心依赖
*  [django-mama-cas](https://github.com/jbittel/django-mama-cas) : A Django Central Authentication Service (CAS) single sign-on server
	*  It implements the CAS 1.0, 2.0 and 3.0 protocols
	*  [Documentation](http://django-mama-cas.readthedocs.io/en/latest/)

### 需求
实现类似apereo/cas的功能，能对接到其他认证后端

### 思路
*  采用django的Authenticate机制,写自己的认证后端
*  关注REMOTE_USER，主要使用单点登录解决方案


### [Authenticating](http://django-mama-cas.readthedocs.io/en/latest/installation.html#authenticating)
One or more [authentication backends](https://pypi.python.org/pypi?:action=browse&show=all&c=475&c=523) must be [installed and configured](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#specifying-authentication-backends) based on your authoritative authentication sources

*  [Django/用户认证](https://zh.wikibooks.org/zh/Django/%E7%94%A8%E6%88%B7%E8%AE%A4%E8%AF%81#.E6.8C.87.E5.AE.9A.E8.AE.A4.E8.AF.81.E5.90.8E.E7.AB.AF)
*  [在Django中自定义身份验证](http://python.usyiyi.cn/django/topics/auth/customizing.html)
	*  AUTHENTICATION_BACKENDS 的顺序很重要，所以如果用户名和密码在多个后台中都是合法的，Django 将在第一个匹配成功后停止处理。如果后台引发PermissionDenied 异常，认证将立即失败。Django 不会检查后面的认证后台。

