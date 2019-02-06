from django.contrib.auth.decorators import login_required
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    HttpResponseBadRequest,
)
from django.template import loader
from django.urls import reverse

from . import models
from .apps import KvkvConfig


def index(request: HttpRequest) -> HttpResponse:
    view = reverse("kvkv:view", args=["val1"])
    # Add current key list
    return HttpResponse(
        f"""index
        {view}
        a
        <a href="e/key1">key1</a>
        <a href="addpair">addpair</a>
        <a href="admin">admin</a>
        {request.user.is_authenticated}
        <a href="{reverse("login")}?next={request.path}">Login</a>
        <a href="{reverse("logout")}?next={request.path}">Logout</a>
        </p>
        <p>{dir(request)}</p>
        """
    )


def e(request: HttpRequest, key: str) -> HttpResponse:
    # Api to post and print values as raw text
    return HttpResponse(f"""{key}""")


@login_required
def addpair(request: HttpRequest) -> HttpResponse:
    user = request.user
    template = loader.get_template("kvkv/addpair.html.dtl")
    return HttpResponse(
        template.render(
            {"user": user, "key": "", "value": ""},
            # Requred for csrf_token
            request,
        )
    )


@login_required
def addpair_post(request: HttpRequest) -> HttpResponse:
    key = ""
    value = ""
    try:
        key = request.POST["key"]
        value = request.POST["value"]
    except KeyError:
        template = loader.get_template("kvkv/addpair.html.dtl")
        return HttpResponse(
            template.render(
                {
                    "user": user,
                    "error_message": "note not given",
                    "key": key,
                    "value": value,
                },
                request,
            )
        )

    models.KeyValue(key=key, value=value).save()
    # return HttpResponseRedirect(KvkvConfig.reverse("view", args=(key,)))
    # Somehow does not work with list: args=[key]
    return HttpResponseRedirect(reverse("kvkv:view", args=(key,)))


def view(request: HttpRequest, key: str) -> HttpResponse:
    try:
        kv = models.KeyValue.objects.get(key=key)
        # TODO: Return 404?
    except models.KeyValue.DoesNotExist as e:
        return HttpResponse("""Data not found""")

    value = kv.value
    return HttpResponse(
        f"""Value for {key}
    {value}"""
    )
