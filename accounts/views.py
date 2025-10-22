from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth import login

# Create your views here.
def signup(request):
    if request.method == 'post':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('log-in')
        else:
            return HttpResponse("Form Submission Failed")
        
        
    form = SignUpForm()
    return render(request,'registration/sign_up.html', {'form':form})
        
    
    