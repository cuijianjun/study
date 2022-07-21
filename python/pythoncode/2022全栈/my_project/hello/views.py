from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

def hello_world(request):
    print(reverse('hello_world'))
    return HttpResponse('hello world')

def hello_china(request):
    return HttpResponse('hello china')

def hello_html(request):
    html = """
        <html>
            <body>
                <h1 style="color: #f00">
                    hello html
                </h1>
            </body>
        </html>
    """
    return HttpResponse(html)

def article_list(request, month):
    """
    :param month: 今年某一个月的文章列表
    """
    return HttpResponse(f'article: {month}')
def search(request):
    """
    GET 参数的获取
    """
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('查询成功')

def render_str(request):
    """
        render_to_string 函数的使用
    """
    templ_name = 'index.html'
    html = render_to_string(template_name=templ_name)
    return HttpResponse(html)