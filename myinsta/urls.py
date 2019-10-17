from django.conf.urls import url
from django.contrib.auth import views 

urlpatterns = [
    url(r'^index/$',views.index,name='insta')
    url(r'^accounts/', include('registration.backends.simple.urls')), 
]    
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
