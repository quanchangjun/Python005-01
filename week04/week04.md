# week04

1. MVC设计模式，前人沉淀下来的编程指导思想。

2. MTV框架模式，常用Django 这个web框架

   模型（Model）、模板（Template）、视图（Views）

3. Django安装

   ~~~cmd
   pip install --upgrade django==2.2.13
   
   python
   import django
   django.__version__
   
   
   >>> import django
   >>> django.__version__
   '3.1.2'
   
   #1、创建django项目
   #2、创建我们的应用程序
   #3、启动
   1、django-admin startproject MyDjango #创建MyDjango项目
   manage.py #命令行工具
   settings.py #项目的配置文件
   
   python manage.py help #查看该工具的帮助
   2、python manage.py startapp index #创建index app
   index/migrations #数据库迁移文件
   index/models.py #模型
   index/views.py #视图
   
   3、启动
   python manage.py runserver
   
   #error:
   django OSError: No translation files found for default language UTF-8.
   #LANGUAGE_CODE = 'en-us'
   LANGUAGE_CODE = 'zh-Hans'
   
   #TIME_ZONE = 'UTC'
   TIME_ZONE = 'Asia/Shanghai'
   
   django django.db.utils.OperationalError: (1049, "Unknown database 'djdb'")
   create database djdb default character set=utf8mb4;
   
   AttributeError: 'str' object has no attribute 'decode'
   
   C:\Users\quanchangjun\AppData\Local\Programs\Python\Python38\lib\site-packages\django\db\backends\mysql\operations.py
   
       def last_executed_query(self, cursor, sql, params):
           # With MySQLdb, cursor objects have an (undocumented) "_executed"
           # attribute where the exact query sent to the database is saved.
           # See MySQLdb/cursors.py in the source distribution.
           query = getattr(cursor, '_executed', None)
           # if query is not None:
               # query = query.decode(errors='replace')
           return query
   
   
   Django version 2.2.13, using settings 'MyDjango.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   
   
   You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
   Run 'python manage.py migrate' to apply them.
   python manage.py migrate
   
   
   python manage.py runserver 0.0.0.0:8080
   ctrl+C
   
   
   C:\Users\quanchangjun\MyDjango>python manage.py runserver
   Watching for file changes with StatReloader
   Performing system checks...
   
   System check identified no issues (0 silenced).
   
   You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
   Run 'python manage.py migrate' to apply them.
   December 20, 2020 - 12:09:24
   Django version 2.2.13, using settings 'MyDjango.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   
   ~~~

   

4. settings.py 项目的配置文件

   配置app列表、配置数据库连接

5. url调度器

   urls.py

   MyDjango/urls.py文件中的urlpatterns列表

   

6. 模块和包

   ~~~ python
   #模块：以.py结尾的python程序
   #包：存放多个模块的目录
   __init__.py包运行的初始化文件，可以是空文件
   
   
   def func1():
       print('import func1')
   
   if __name__ == '__main__':
       func1()
   
       
   from MyPackage import Module1 as M1
   from . import Module1
   from .Pkg2 import Module2 as M2
   
   ~~~

   

7. 带变量的url

   ~~~python
   #带变量的url
   path('<int:year>',views.year)
   path('<int:year>/<str:name>',views.name)
   
   #正则匹配
   re_path('(?P<year>[0-9]{4}).html',views.myyear,name='urlyear')
   
   #自定义过滤器
   path('<myint:year>',views.year)
   
   
   ~~~

   

8. View视图

9. 模型

   ```shell
   Django去操作数据模型
   from django.db import models
   class Person(models.Model):
       id = models.IntegerField(primary_key=True)
       first_name = models.CharField(max_length=30)
       last_name = models.CharField(max_length=30)
       
   
   1、写脚本到models.py里
   
   2、__init__.py
   import pymysql
   pymysql.install_as_MySQLdb()
   
   3、然后分别在终端执行下面：
   python manage.py makemigrations
   python manage.py migrate
   
   
   ```

   

10. Douban

    ``` shell
    python manage.py startapp Douban
    
    python manage.py inspectdb >models.py
    
    python manage.py runserver
    
```
    
    