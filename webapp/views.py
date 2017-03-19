from django.shortcuts import render
from django.views.generic import ListView
from webapp.models import Profile

from .forms import ContactForms


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
    confirm_message = None


    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        user_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        phone_number = form.cleaned_data['phone_number']
        location = form.cleaned_data['location']
        confirm_message = "Thanks for signing up, we will get back to you shortly"
        # is_registered = True

        # Create user object

        user_obj = Profile(first_name=first_name,last_name=last_name,user_name=user_name,
                           email= email, password=password,
                           phone_number=phone_number, location=location)
        user_obj.save()

        form = None

    context = {
        'form': form,
        'confirm_message': confirm_message,
        # 'is_registered': is_registered
    }
    return render(request, template, context)

# def showdatat(request):
#
#     all_users = Profile.objects.all()
#
#     return render(request, 'users/showdata.html', {'all_users': all_users})


