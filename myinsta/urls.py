from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    url('^$',views.well,name='well'),
    url('^new/post$',views.new_post,name='new_post'),
    url(r'^accounts/profileform', views.profile_form, name='profileform'),
]
