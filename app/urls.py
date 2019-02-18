# from django.conf.urls import include, url
from django.urls import include, path, re_path

# from django.views.generic.base import RedirectView

from . import views
from .apps import KvkvConfig

app_name = KvkvConfig.label
urlpatterns = [
    path("", views.index, name="index"),
    # Entry: Api to post and print values as raw text
    path("e/<key>", views.e, name="e"),
    path("addpair", views.addpair, name="addpair"),
    path("addpair_post", views.addpair_post, name="addpair_post"),
    path("view/<key>", views.view, name="view"),
    path("list", views.list_, name="list"),
    path("edit/<key>", views.edit, name="edit"),
]
