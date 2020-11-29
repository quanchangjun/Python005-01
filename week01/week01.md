# week01

### python版本选择

pyhon 3.X版本，比如python3.7、python3.8

docs.python.org

工作中常用版本：python3.7

https://docs.python.org/zh-cn/3.7/whatsnew/3.7.html

训练营使用的是python3.7.9版本

只安装一个Python解释器

PATH环境变量设置

```python
python
exit()
python -V
```

venv 虚拟环境

pip命令：方便安装第三方库

python3 -V

ls /Library/Frameworks/Python.framework/Versions/3.7/bin

ipython

```python
python
str1='hello,world'
print(str1)
type(str1)
str1.upper()
help(str)

pip3 install ipython
```



> 一般开发流程
>
> 1. 搞清需求
> 2. 编写源代码
> 3. 使用python解释器转换为目标diam
> 4. 运行程序
> 5. 测试
> 6. 修复错误
> 7. 再运行、测试
> 8. 。。。

### 数据类型

1. 基础数据类型：

   None 空对象

   boolean 布尔值

   数值类型（整数、浮点数、复数）

   序列 （字符串、列表、元组）

   集合 字典

   可调用 函数

   ``` python
   var1 = NONE
   
   print(type(var1))
   
   var is null
   var2=123
   var2 is None 
   x=10
   y=20
   x==y
   x>y
   x!=y
   Ture/False
   'abc'
   "abc"
   x="I'm xxyy"
   字符串内置的方法
   x.capitalize()
   y=['a','b','c']
   y.append('e')
   z=('a','b','c')
   
   ```

   

2. 高级数据类型

   collections 容器数据类型

   nametuple() 命名元组

   deque 双端队列

   Counter 计数器

   OrderedDict 有顺序的字典

   https://docs.python.org/zh-cn/3.7/library/index.html

   

### 控制流

```python
if Ture:
    print("Ture")
if False:
    print('nothing')
num=100
if num>50:
    pirnt('xxx')
else:
    print('yyy')

num=10
while num != 0:
    print(num)
    num=num-1

list1 = ['a','b','c']
len(list1)
i=0
while i<len(list1):
    print(list1[i])
    i+=1

for i in list1:
    print(i)

python中for循环可以用来迭代的
多使用python风格的代码
```



### 常见模块

1. time
2. datetime
3. logging
4. random
5. json
6. pathlib
7. os.path

python的标准库

python的第三方模块

多个函数组成模块

函数、模块、包



re 正则表达式

https://docs.python.org/zh-cn/3.7/library/re.html

prog=re.compile(pattern)

result=prog.match(string)

等价于

result=re.match(pattern,string)

正则表达式

检索、替换、提取子串