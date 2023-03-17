from django.urls import re_path

from .views import do_something


urlpatterns = [
    re_path(r"^enqueue-an-on-demand-task/", do_something, name="enqueue-on-demand"),
]
