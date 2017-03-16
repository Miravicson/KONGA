from django.views.generic import DetailView, ListView


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


class Signup(ListView):
    template_name = 'webapp/signup.html'

    def get_queryset(self):
        return
