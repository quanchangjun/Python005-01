# week02

## 前端知识

* W3C规定网页由3部分组成，即结构、表现、行为

* html（结构）、css样式（表现）、js脚本(定义行为)

* jquery.js，ajax，jQuery的dollar.ajax方法，异步更新网页数据

* get方式请求内容，post用于登录

* 浏览器，工具查看network，Headers主要关注：Request URL、status code、Request Method、Cookie、Host、Referer、User-Agent

* 文字、链接、图片

  ~~~ html
  <span>文字</span>
  <a>链接</a>
  <img>图片
  ~~~

  

> 1. 提出需求
> 2. 编码
> 3. 



## requests

1. 增加程序健壮性

   * with open(上下文管理器)

   ~~~python
   file1 = open('a.txt',encoding='utf8')
   try:
       data = file1.read()
   finally:
       file1.close()
       
   
   with open('a.txt',encoding='utf8') as file2:
       data = file2.read()
   
   
   ~~~

   

   * 异常捕获

   参考：https://docs.python.org/zh-cn/3.6/library/exceptions.html
   Traceback函数以及它的跟踪

~~~python
#StopIteration异常示例：
gennumber = (i for i in range(0,2))
print(next(gennumber))
print(next(gennumber))

try:
    print(next(gennumber))
except StopIteration:
    print('最后一个元素')
    

try:
    1/0
except Exception as e:
    print(e) #输出异常信息

    
try:
    1/0
except Exception as e:
    try:
        1/0
    except Exception as f:
        pass
    print(e) #输出异常信息
    
    
~~~

pip3 install pretty_errors

pip install lxml



编程规范：

PEP-8

Google Python风格指引



自顶向下设计

* 从整体分析一个比较复杂的大问题
* 分析方法可以重用
* 拆分到你能解决的范畴



