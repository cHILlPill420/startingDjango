from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
#from . import forms
from first_app.forms import NewSite, NewRecord
# Create your views here.

def index(request):
    my_dict = {'insert_me' : "hello I'm from views.py html=firstapp/index!"}
    return render(request, 'first_app/index.html', context = my_dict)

def dbdb(request):    
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'first_app/datafromdb.html', context = date_dict)

def form_view(request):
    form = NewSite()
    if request.method == "POST":
        form = NewSite(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        raise forms.ValidationError("Not valid")

    # form = forms.FormNorm()
    # if request.method == 'POST':
    #     form = forms.FormNorm(request.POST)
    #     if form.is_valid():
    #         print('Validation successful')
    #         print('NAME: '+form.cleaned_data['name'])
    #         print('EMAIL: '+form.cleaned_data['email'])
    #         print('TEXT: '+form.cleaned_data['text'])
    return render(request, 'first_app/form.html', {'form':form})
#def index2(request):
    #return HttpResponse("<em> 2nd index </em>")

# def form_view_date(request):
#     form2 = NewRecord()
#     if request.method == "POST":
#         if form2.is_valid():
#             form2.save(commit = True)
#             return index(request)
#         raise forms.ValidationError("invalid")
#     return render(request, 'first_app/form.html', {'form2':form2})

def relative(request):
    return render(request, 'first_app/relative_url_templates.html')