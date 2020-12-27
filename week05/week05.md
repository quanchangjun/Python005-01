



# week05

1. 中间件

   + 缓存

     缓存的分类：

     * 本地缓存

     * 分布式缓存

     缓存与数据库的同步方式：

     * 双写：数据库和Redis各写一份
     * 消息队列：写数据库和消息队列，消息队列再同步到Redis
     * Mysql binlog：使用Mysql binlog重放同步到Redis

     缓存有可能带来问题：

     * 缓存穿透
     * 缓存并发
     * 缓存雪崩

   + 消息队列
     * 连接和缓存

2. redis

   非关系型数据库，NoSql数据库

   redis的对象类型：

   * 字符串

     int、embstr、raw

   * 列表(list)

   * 哈希(hash)

   * 集合(set)

   * 有序集合(zset)

   ~~~shell
   cat /etc/redhat-release
   
   gcc --version
   
   [root@ks01 ~]# cat gcc8.sh
   #!/bin/bash
   yum install centos-release-scl scl-utils-build
   yum list all --enablerepo='centos-sclo-rh'
   yum install -y devtoolset-8-toolchain
   scl enable devtoolset-8 bash
   gcc --version
   
   #./configure
   make
   make install
   
   exit
   
   which redis-server
   which redis-client
   redis.config
   
   [root@ks01 ~]# which redis-server
   /usr/local/bin/redis-server
   
   [root@ks01 ~]# which redis-cli
   /usr/local/bin/redis-cli
   
   redis.conf
   requirepass
   bind
   
   redis-server /etc/redis.conf
   
   [root@ks01 ~]# ss -ntpl |grep 6379
   LISTEN     0      128          *:6379                     *:*                   users:(("redis-server",pid=19473,fd=6))
   
   [root@ks01 ~]# redis-cli
   127.0.0.1:6379> autho
   shutdown
   
   
   
   
   list
   数据可以重复
   set
   数据不重复
   集合运算（交集、并集、差集）
   
   
   ~~~

   

3. Redis的重要机制

   * 生存时间

   * 主从复制

   * 哨兵

     

4. RabbitMQ

   ```shell
   rpm -Uvh https://download.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
   yum install erlang
   #rpm -Uvh https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.8/rabbitmq-server-3.6.8-1.el7.noarch.rpm
   yum install rabbitmq-server
   rabbitmq-plugins enable rabbitmq_management
   
   localhost:15672
   guest/guest
   
   
   
   
   ```

5. RPC(远程过程调用)

   RabbitMQ就是一个RPC软件