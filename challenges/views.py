from django.shortcuts import render
from helpers.better_enum import BetterEnum
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.urls import reverse


class MonthlyChallenges(BetterEnum):
    january = 'Eat meat'
    february = 'Walk a lot'
    march = 'Gym a lot'
    april = 'Read a lot'
    may = 'Run a lot'
    june = 'Relax a lot'
    july = 'Take a lot of sauna'
    august = 'Study a lot'
    september = 'No meat month'
    october = 'Stoptober'
    november = 'No nut November'
    december = 'Cheat month'


def index(request: HttpRequest) -> HttpResponse:
    html_list_item = ''
    for month in MonthlyChallenges:
        html_list_item += (
            f'<li><a href="{reverse("monthly-challenge", args=[month.name])}">{month.name.capitalize()}</a></li>'
        )
    return HttpResponse(f'<ul>{html_list_item}</ul>')


def monthly_challenge_by_number(request: HttpRequest, month: int):
    for index, member in enumerate(MonthlyChallenges):
        if index == (month - 1):
            return HttpResponseRedirect(reverse("monthly-challenge", args=[member.name]))
    return HttpResponseNotFound("<h1>No month is represented by that number</h1>")


def monthly_challenges(request: HttpRequest, month: str) -> HttpResponse:
    try:
        challenge_text = f'<h1>{MonthlyChallenges.from_name(month).value}</h1>'
        return HttpResponse(challenge_text)
    except ValueError:
        return HttpResponseNotFound("<h1>No month with that name exists</h1>")
