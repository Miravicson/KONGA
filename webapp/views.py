from django.shortcuts import render
from django.views.generic import ListView

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
        print(form.cleaned_data['email'])
        confirm_message = "Thanks for signing up, we will get back to you shortly"
        form = None

    context = {
        'form': form,
        'confirm_message': confirm_message,
    }
    return render(request, template, context)


