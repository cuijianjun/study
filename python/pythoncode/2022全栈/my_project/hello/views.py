from django.urls import reverse
from django.http import HttpResponse

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
