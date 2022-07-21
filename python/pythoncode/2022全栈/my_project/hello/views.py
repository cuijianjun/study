from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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

def http_request(request):
    """
        请求练习
    """
    # 1. 请求方式
    print(request.method)
    # 2. 请求头信息 
    header = request.META
    ua = request.META.get('HTTP_USER_AGENT', None)
    print(request.headers)
    print(request.headers['User-Agent'])
    print(request.headers['user-agent'])
    # 3. 获取参数
    name = request.GET.get('name', '')
    return HttpResponse('响应')

def http_response(request):
    # resp = HttpResponse('响应内容', status = 201)
    # resp.status_code = 204
    # print(resp.status_code)
    # return resp
    user_info = {
        'name': '张三',
        'age': 34
    }
    return JsonResponse(user_info)

def no_data_404(request):
    """404页面"""
    return HttpResponse('404')

def article_detail(request, article_id):
    """
        文章详细，ID是从1000开始的整数
        ：params article_id:文章ID
    """
    if article_id < 1000:
        # return HttpResponseRedirect('/hello/404/')
        # return HttpResponseRedirect(reverse('no_data_404'))
        return redirect('no_data_404')
    return HttpResponse(f'文章{article_id}的内容')