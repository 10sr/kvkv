# from django.conf.urls import include, url
from django.urls import include, path, re_path
# from django.views.generic.base import RedirectView

from . import views
from .apps import KvkvConfig

app_name = KvkvConfig.label
urlpatterns = [
    path("", views.index, name="index"),
    path("e/<key>", views.e, name="e"),
    path("addpair", views.addpair, name="e"),
]
