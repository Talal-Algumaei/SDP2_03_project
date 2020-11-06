from django.shortcuts import render
from .forms import UserCreateForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class UserFormView(View):
    form_class = UserCreateForm
    template_name = 'registration_form.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
             
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            return redirect('login')
        else:
            messages.info(request,form.errors.get('password2'))
            messages.info(request,form.errors.get('email'))
            messages.info(request,form.errors.get('username'))
            
        return render(request, self.template_name, {'form': form})
   


class UserLogin(View):
    form_class = UserCreateForm
    template_name = 'login_page.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
            form = self.form_class(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'username or password is incorrect')

            return render(request, self.template_name, {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')


def user_page(request):
    context = {}
    return render(request, 'charts.html', context)


