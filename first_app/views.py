from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me' : "hello I'm from views.py html=firstapp/index!"}
    return render(request, 'first_app/index.html', context = my_dict)

#def index2(request):
    #return HttpResponse("<em> 2nd index </em>")