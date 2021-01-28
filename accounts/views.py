from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
                
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('registration failed')
                
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})




def logout(request):
    if request.method=='POST':
        logout(request)
        return HttpResponseRedirect('login')


def home(request):
    #return HttpResponse('this is HOME of {{request.user.username}} <p>Your Username is : {{request.user}} </p>')
    return render(request, 'index.html', {
        'user': request.user,
        })
