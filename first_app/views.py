from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import AccessRecord, Topic, Webpage
#from . import forms
from first_app.forms import NewSite, UserForm, UserProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    my_dict = {'insert_me' : "hello I'm from views.py html=firstapp/index!", 'number': 10}
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

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password) #settings.py-> PASSWORD_HASHER & validators used
            user.save()
            
            profile = profile_form.save(commit = False) #False because we want to perform task like relating one to one with user, True lets it directly save to database
            profile.user = user #relating profile and user in one to one fashion

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
           print(user_form.error,profile_form.error)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'first_app/registration.html',
                            {'user_form':user_form,
                             'profile_form':profile_form,
                             'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("someone tried to login using:- username: {} password: {}".format(username,password))
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'first_app/login.html')
        #return HttpResponseRedirect(reverse('first_app:loginn'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('Logged in yo')