import django


from django.urls import path
from hello.views import hello_world, hello_china, hello_html
urlpatterns = [
    path('world/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
    path('html/', hello_html, name='hello_html'),
]