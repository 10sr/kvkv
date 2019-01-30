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
        <a href="v/test/page">test/page</a>
        <a href="v/hoe">hoe</a>
        <a href="admin">admin</a>
        <p>{dir(request)}</p>
        """
    )
