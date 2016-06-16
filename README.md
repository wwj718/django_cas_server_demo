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


