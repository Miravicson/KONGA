from django.conf.urls import url
from webapp.views import Index, Rotatecard, signup

app_name = 'konga'
urlpatterns = [
    url(r'^$', Index.as_view(), name='home'),
    url(r'^rotatecard/$', Rotatecard.as_view(), name='rotate'),
    url(r'^signup/$', signup, name='signup'),
    # url(r'^showdata/$', showdata, name='showdata')
]
