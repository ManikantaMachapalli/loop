from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'Mani'}
    return render(request,'loop.html',d)