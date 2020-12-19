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
   
   
   
   ~~~

   

4. settings.py

5. url调度器

   urls.py

   

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

   