from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout



def signup_view(request):
    form = UserCreationForm()
    if form.is_valid():
            form.save()
            #log the user in
            login(request,user)
            return redirect('hello.html')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('login.html')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
    
    