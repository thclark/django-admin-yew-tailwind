from django.contrib import admin
from django.urls import include, re_path
from django.views.generic.base import RedirectView

from yewtail import urls as yewtail_urls
from .example import urls as example_urls


admin.autodiscover()


urlpatterns = [
    # Include the django admin so we can use it with the example app
    re_path(r"^admin/", admin.site.urls),
    # Include the yewatil urls (if we add any! At the time of writing it's empty)
    re_path(r"^example-yewtail/", include(yewtail_urls)),
    # Include your own app URLs
    re_path(r"^example-app-urls/", include(example_urls)),
    # Redirecting to the admin for convenience when using the example app :)
    re_path(r"^", RedirectView.as_view(url="admin/")),
]
