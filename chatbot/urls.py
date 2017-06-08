from django.conf.urls import url

from . import views

# linebot callback api.
urlpatterns = [
    url('^callback/', views.callback),
]