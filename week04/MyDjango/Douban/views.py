from django.shortcuts import render
from .models import T1
from django.db.models import Avg
from .models import Movie as mv


def books_short(request):
    # 从models 取数据传给template
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = f"{T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f}"
    # 情感倾向
    sent_avg = f"{T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"
    
    # 正向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte':0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt':0.5}
    minus = queryset.filter(**condtions).count()

    return render(request,'result.html',locals())

def index_page(request):
    n = mv.objects.all().filter(n_star__gt=3)

    return render(request,'index.html',locals())