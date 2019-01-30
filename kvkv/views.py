from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    HttpResponseBadRequest,
)


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        f"""index
        <a href="e/key1">key1</a>
        <a href="addpair">addpair</a>
        <a href="admin">admin</a>
        <p>{dir(request)}</p>
        """
    )


def e(request: HttpRequest, key: str) -> HttpResponse:
    return HttpResponse(
        f"""Add key {key}"""
    )


def addpair(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        f"""Page used by human to add key value pair."""
    )
