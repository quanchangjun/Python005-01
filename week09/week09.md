# week09

1. 前后端分离

   Rest API(Representational State Transfer)，直译为”表现层状态转化“

   Rest API 风格指引或者规约

   Rest是面向资源的

   

2. Django实现REST API

   ~~~shell
   python -m pip install --upgrade pip
   
   pip3 install djangorestframework
   #序列化
   from rest_framework import serializers
   
   #Views
   #FBV vs CBV
   
   pip install pygments
   python manage.py runserver
   
   #修改django的settings.py，添加rest_framework
   python manage.py makemigrations
   python manage.py migrate
   
   python manage.py createsuperuser --email a@a.com --username user1
   
   pip3 install httpie
   http get http://127.0.0.1:8000/users/1/
   
   C:\Windows\system32>http get http://127.0.0.1:8000/users/1/
   HTTP/1.1 200 OK
   Allow: GET, HEAD, OPTIONS
   Content-Length: 115
   Content-Type: application/json
   Date: Sun, 24 Jan 2021 03:49:59 GMT
   Server: WSGIServer/0.2 CPython/3.8.5
   Vary: Accept, Cookie
   X-Frame-Options: SAMEORIGIN
   
   {
       "id": 1,
       "snippets": [
           "http://127.0.0.1:8000/snippets/1/"
       ],
       "url": "http://127.0.0.1:8000/users/1/",
       "username": "admin"
   }
   
   
   http GET http://127.0.0.1:8000/api/v2/articles/3/
   http -a admin:admin PUT http://127.0.0.1:8000/api/v2/articles/3/ article='hello'
   http -a admin:admin DELETE http://17.0.1:8000/api/v2/articles/3/
   
   
   pip3 install django-filter
   pip3 install notifications
   python manage.py migrate notifications
   
   pip install django-notifications-hq
   pip install djangorestframework-jwt
   pip install coreapi pyyaml
   
   python manage.py makemigrations
   python manage.py migrate
   
   
   
   
   ~~~

   

   

   