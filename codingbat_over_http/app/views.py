from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def near_hundred_view(request: HttpRequest, n: int) -> HttpResponse:
    return HttpResponse((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


def string_splosion_view(request: HttpRequest, string: str) -> HttpResponse:
    result = ""
    for i in range(len(string)):
        result += string[: i + 1]
    return HttpResponse(result)


def cat_dog_view(request: HttpRequest, string: str) -> HttpResponse:
    dogCount = string.count("dog")
    catCount = string.count("cat")
    return HttpResponse(dogCount == catCount)


def lone_sum_view(request: HttpRequest, a: int, b: int, c: int) -> HttpResponse:
    if a != b and b != c and a != c:
        return HttpResponse(a + b + c)
    elif a == b and a != c:
        return HttpResponse(c)
    elif a == c and a != b:
        return HttpResponse(b)
    elif b == c and a != b:
        return HttpResponse(a)
    else:
        return HttpResponse(0)
