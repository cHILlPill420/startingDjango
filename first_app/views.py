from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
from . import forms
# Create your views here.

def index(request):
    my_dict = {'insert_me' : "hello I'm from views.py html=firstapp/index!"}
    return render(request, 'first_app/index.html', context = my_dict)

def dbdb(request):    
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'first_app/datafromdb.html', context = date_dict)

def form_view(request):
    form = forms.FormNorm()
    if request.method == 'POST':
        form = forms.FormNorm(request.POST)
        if form.is_valid():
            print('Validation successful')
            print('NAME: '+form.cleaned_data['name'])
            print('TEXT: '+form.cleaned_data['text'])
    return render(request, 'first_app/form.html', {'form':form})
#def index2(request):
    #return HttpResponse("<em> 2nd index </em>")