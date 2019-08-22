from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterNewUserForm
# Create your views here.


def register_user(request):
    template = './register.html'
    context = {}
    if request.method == 'POST':
        form = RegisterNewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template, {"message": "User Saved", "clase": "alert-success text-center"})
        else:
            return render(request, template, {"message": "Error check all fields", "clase": "alert-danger text-center"})
    return render(request, template, context)


def login_user(request):
    template = './login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # success
            login(request, user)
            return  redirect('menu')
        else:
            # error
            return  render(request, template, {"message": "Invalid credentials", "clase": "alert-danger"})
    return render(request, template)

def logout_view(request):
    logout(request)
    
    return  redirect('login_auth')
    # Redirect to a success page.