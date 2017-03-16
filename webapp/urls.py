from django.conf.urls import url
from webapp.views import Index, Rotatecard, Signup

app_name = 'konga'
urlpatterns = [
    url(r'^$', Index.as_view(), name='home'),
    url(r'^rotatecard/$', Rotatecard.as_view(), name='rotate'),
    url(r'^signup/$', Signup.as_view(), name='signup')
]
