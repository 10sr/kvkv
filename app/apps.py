from typing import Iterable

import django.apps
from django.urls import reverse


class KvkvConfig(django.apps.AppConfig):
    name = "app"
    label = "kvkv"

    @classmethod
    def reverse(cls, name: str, args: Iterable[str] = ()) -> str:
        return reverse(f"{cls.label}:{name}", args)
