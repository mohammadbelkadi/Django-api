from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


class squaringView(View):
    def get(self, request, number):
        print(request.__dir__())
        return HttpResponse(number ** 2)

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello World!')
