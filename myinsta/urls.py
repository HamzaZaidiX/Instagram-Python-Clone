from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    url('^$',views.welc,name='well'),
    url('^new/post$',views.new_post,name='new_post'),
    url(r'^accounts/profileform', views.profile_form, name='profileform'),
    url(r'^profile/',views.profile,name='profile'),
    # url(r'^like/(\d+)',views.likes,name= 'likes'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
