from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    url('^$',views.well,name='well'),
]
