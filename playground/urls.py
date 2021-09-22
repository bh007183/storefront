from django.urls import path
from . import views


urlpatterns = [
    path("hello/", views.say_hello),
    path("html/", views.send_html),
    path("data/", views.send_html_data)
]