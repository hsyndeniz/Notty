from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from note import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', views.profile),
    url(r'^$', include('note.urls')),


]

urlpatterns += staticfiles_urlpatterns()