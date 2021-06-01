# week03

1. mysql安装

   * 企业级MySQL部署在Linux操作系统上

   * mysql企业版、mysql社区版、MariaDB

   * dev.mysql.com

     ~~~ linux
     arch
     cat /etc/redhat-release
     yum install mysql57-community-
     yum install *.rpm
     
     #避免yum update更新，使用yum remove删除yum包索引
     yum remove mysql57-community-release-el7-10.noarch
     
     systemctl start mysqld.service
     systemctl enable mysqld
     systemctl status mysqld.service
     
     #service mysqld start
     
     #通过下面查看，确认安装的是mysql社区版
     rpm -qa|grep -i 'mysql'
     
     grep 'password' /var/log/mysqld.log |head -1
     
     mysql -uroot -p
     alter user 'root'@'localhost' identified by '123456';
     show variables like 'validate_password%';
     set global validate_password_policy=0;
     quit;
     
     mysql -uroot -p
     show variables like '%character%';
     show variables like 'collation_%';
     #mysql 中的utf8不是UTF-8字符集
     
     #字符集 ASCII、LATIN、GBK、utf8、utf8mb4
     #utf8 一个字符占3个字节
     #utf8mb4 对应utf-8字符集，一个字符占4个字节
     vim /etc/my.cnf
     [client]
     default_character_set = utf8mb4
     
     [mysql]
     default_character_set = utf8mb4
     
     [mysqld]
     interactive_timeout = 28800
     wait_timeout = 28800
     max_connections = 1000
     character_set_server = utf8mb4
     init_connect = 'SET NAMES utf8mb4'
     character_set_client_handshake = FALSE
     collation_server = utf8mb4_unicode_ci
     
     systemctl restart mysqld
     
     #_ci不区分大小写、_cs区分大小写
     utf8_general_ci
     utf8mb4_unicode_ci
     
     
     
     ~~~

     

2. python连接mysql

   * Python Database API、DB-API

   * MySQLdb 是Python2的包，适用于mysql5.5 和python2

   * pyton3 安装的mysqldb包叫mysqlclient，加载的依然是mysqldb

   * pip install mysqlclient

   * import MySQLdb

     ```shell
     pip3 install pymysql #使用pip3来安装第三方模块
     pip install mysql-connector-python
     
     #使用ORM
     pip install sqlalchemy
     
     #如果安装了anaconda,可以使用下面命令查看是否安装
     conda list pymysql
     conda list sqlalchemy
     
     mysql -uroot -p
     create database testdb;
     grant all privileges on testdb.* to 'testuser'@'%' identified by 'testpass';
     
     
     ```

     

3. mysql常用操作

   ~~~ mysql
   create table book1(
   book_id int not null auto_increment,
   type_id int not null,
   book_name varchar(255) character set utf8 collate utf8_general_ci not null,
   primary key (book_id) using BTREE
   ) comment '书信息表'
   engine=Innodb character set=utf8 collate=utf8_general_ci
   ;
   
   
   select distinct book_id,book_name,count(*) as cnt #5
   from book join author on book.sn_id=author.sn_id #1
   where pages>500 #2
   group by book.book_id #3
   having cnt >10 #4
   order by number #6
   limit 5 #7
   
   ~~~

   

聚合函数

非关联子查询
关联子查询

exists
in
小表驱动大表

连接

事务
要么全执行，要么全不执行
事务的特性ACID
A	原子性（Atomicity)
C	一致性(Consistency)
I	隔离性(Isolation)
D	持久性(Durability)

事务的隔离级别
读未提交：允许读到未提交的数据
读已提交：只能读到已经提交的内容
可重复读：同一事务在相同查询条件下两次查询得到的数据结果一致
可串行化：事务进行串行化，但是牺牲了并发性能

mysql：可重复读

oracle：读已提交

~~~ mysql
show variables like 'autocommit';
set autocommit=0;
mysql默认是隐式提交
oracle 需要明确写commit显示提交

begin
commit
rollback

~~~



4. python操作mysql数据库

   ~~~ python
   #pymysql 实现对mysql的增删改查
   cursor.rowcount
   
   cursor.execute(sql,value)
   cursor.executemany(sql,value)
   
   fetchone
   fetchall
   fetchmany
   
   #sqlalchemy
   #魔术方法
   __repr__(self)
   
   #使用ORM
   #业务逻辑层
   #持久层
   #数据库层
   
   echo=True
   session.query(Book_table).all()
   session.query(Book_table).first()
   
   for result in session.query(Book_table.book_name).order_by(Book_table.book_id):
       
   from sqlalchemy import and_, or_, not_
   
   print([result.book_name for result in query])
   
   #连接池
   
   
   
   ~~~

   

5. 调优

   结合业务的调优

   