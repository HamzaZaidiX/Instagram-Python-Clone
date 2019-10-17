from django.conf.urls import url

urlpatterns = [
    url(r'^accounts/', include('registration.backends.simple.urls')),
]