from django.conf.urls import url

urlpatterns = [
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
