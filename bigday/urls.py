from django.conf.urls import url, include
from django.contrib import admin
from bigday.views import contact, thanks, home, volunteer, donate

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', contact),
    url(r'^thanks/$', thanks),
    url(r'^donate', donate),
    url(r'^volunteer', volunteer),
#   url(r'^volunteer/$', volunteer),
#    url(r'^thanks/$', views.thanks, name='thanks'),
#url(r'^contact/$', include('bigday.urls')),
 #   url(r'^contact/$', views.contact),
  #  url(r'^paytm/', include('paytm.urls')),
   # url('^accounts/', include('django.contrib.auth.urls')),
]
