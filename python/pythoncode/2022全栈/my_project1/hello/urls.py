import django


from django.urls import path, re_path
from hello.views import render_str, hello_world, hello_china, hello_html, article_list, search, index, HomeView
urlpatterns = [
    path('world/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
    path('html/', hello_html, name='hello_html'),
    # path('article/<int:month>', article_list, name='article_list'),
    re_path(r'^article/(?P<month>0?[1-9]|1[012])/$', article_list, name='article_list'),
    path('search/', search, name='search'),
    path('render/str/', render_str, name='render_str'),
    path('index/', index, name='index'),
    path('home/', HomeView.as_view(), name='home'),
]