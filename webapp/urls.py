from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from webapp.views import Index, Rotatecard, signup, login, verify, saveorder, UserList

app_name = 'konga'
urlpatterns = [
    url(r'^$', Index.as_view(), name='home'),
    url(r'^rotatecard/$', Rotatecard.as_view(), name='rotate'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^verify/$', verify, name='verify'),
    url(r'^login/$', login, name='login'),
    url(r'^saveorder(?P<userid>\d+)/$', saveorder, name='saveorder'),
    url(r'^kongaapi/$', UserList.as_view(), name='kongaapi'),
]

urlpatterns = format_suffix_patterns(urlpatterns)