from django.conf.urls import url
from django.contrib.auth import views 

urlpatterns = [
    url('^$',views.index,name='insta')
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}), 
]    
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
