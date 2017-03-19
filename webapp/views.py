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

# @csrf_protect
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password1'],
#                 email=form.cleaned_data['email']
#             )
#             return HttpResponseRedirect('/register/success/')
#     else:
#         form = RegistrationForm()
#     variables = RequestContext(request, {
#         'form': form
#     })
#
#     return render_to_response(
#         'registration/register.html',
#         variables,
#     )
#
#
# def register_success(request):
#     return render_to_response(
#         'registration/success.html',
#     )
#
#
# def logout_page(request):
#     logout(request)
#     return HttpResponseRedirect('/')
#
#
# @login_required
# def home(request):
#     return render_to_response(
#         'home.html',
#         {'user': request.user}
#     )
