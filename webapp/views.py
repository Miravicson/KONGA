from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Profile
from .forms import ContactForms, LoginForms, OrdersForms


# Create your views here.
class Index(ListView):
    # model =
    template_name = 'webapp/index.html'

    def get_queryset(self):
        return


class Rotatecard(ListView):
    template_name = 'webapp/rotating-card.html'

    def get_queryset(self):
        return


def signup(request):
    template = 'webapp/signup.html'

    form = ContactForms(request.POST or None)
    form2 = LoginForms(request.POST or None)
    confirm_message = None
    error_message = None
    # user_name = request.POST.get('user_name')
    # user = authenticate(username=user_name)

    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        user_name = form.cleaned_data['user_name']
        email = form.cleaned_data['email']
        password = make_password(form.cleaned_data['password'])
        phone_number = form.cleaned_data['phone_number']
        location = form.cleaned_data['location']

        # Create user object
        try:
            user_obj = User(username=user_name, password=password, email=email, first_name=first_name,
                            last_name=last_name)
            user_obj.save()
            profile_obj = Profile(first_name=first_name, last_name=last_name, user_name=user_name,
                                  email=email, password=password, phone_number=phone_number, location=location)
            profile_obj.save()
            form = None
            confirm_message = "Thanks for signing up, we will get back to you shortly"
        except Exception:
            error_message = "Choose a different username"

    context = {
        'form': form,
        'form2': form2,
        'confirm_message': confirm_message,
        'error_message': error_message,

    }
    return render(request, template, context)


def verify(request):
    form2 = LoginForms(request.POST or None)
    if form2.is_valid():
        user_name = form2.cleaned_data['user_name']
        print(user_name)

        password = form2.cleaned_data['password']
        print(password)
        user = authenticate(username=user_name, password=password)
        if user is not None:
            template = 'webapp/loginscreen.html'
            form3 = OrdersForms(request.POST or None)

            context = {
                'form3': form3,
                'user': user,
            }
            return render(request, template, context)
        else:
            return HttpResponse('incorrect login details')


def login(request):
    form2 = LoginForms(request.POST or None)
    template = 'webapp/login.html'
    context = {
        'form2': form2
    }
    return render(request, template, context)
