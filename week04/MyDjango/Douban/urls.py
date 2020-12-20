from django.urls import path
# 从当前app下访问views
from . import views

urlpatterns = [
    # path('index',views.books_short),
    path('index',views.index_page),
]