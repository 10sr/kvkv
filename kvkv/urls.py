# from django.conf.urls import include, url
from django.urls import include, path, re_path
# from django.views.generic.base import RedirectView

from . import views
from .apps import KvkvConfig

app_name = KvkvConfig.label
urlpatterns = [
    path("", views.index, name="index"),
]
