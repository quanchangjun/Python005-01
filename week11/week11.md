# week11

1. Scrapy 异步编程

   单任务同步、多任务同步、多任务异步

   

2. 多进程

   ~~~python
   import os
   os.fork()
   
   
   from multiprocessing import Process
   
   if __name__ == "__main__":
       p=Process(target=run)
       p.start()
       p.join()
   
   ~~~

   

3.进程间的通信

队列、管道、共享内存

~~~python
#队列
from multiprocessing import Process,Queue

def f(q):
    q.put([42,None,'hello'])

if __name__ == "__main__":
    q=Queue()
    p=Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()

    
    
    
#管道是队列的一个底层工具
from multiprocessing import Process,Pipe

#共享内存
from multiprocessing import Process,Value,Array

~~~



4.锁

5.多进程：进程池

~~~python
from multiprocessing.pool import Pool
from time import sleep,time
import random
import os


~~~

6.多线程

~~~python
import threading

thread1 = threading.Thread(target=start)
print(thread1.is_alive())

阻塞、被阻塞
同步、异步
~~~

7.多线程：线程锁

基本的锁：

普通锁(lock)、嵌套锁(rlock)

高级的锁：

条件锁、信号量、事件、定时器



8.多线程：队列

~~~python
import queue

~~~



9.多线程：线程池

10.GIL锁

CPU密集型

IO密集型

