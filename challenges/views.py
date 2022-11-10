from django.shortcuts import render
from helpers.better_enum import BetterEnum
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


class MonthlyChallenges(BetterEnum):
    january = 'Eat meat'
    february = 'Walk a lot'
    march = 'Gym a lot'
    april = 'Eat meat'
    may = 'Walk a lot'
    june = 'Gym a lot'
    july = 'Eat meat'
    august = 'Walk a lot'
    september = 'Gym a lot'
    october = 'Eat meat'
    november = 'Walk a lot'
    december = 'Gym a lot'


def monthly_challenge_by_number(request: HttpRequest, month: int):
    for index, member in enumerate(MonthlyChallenges):
        if index == (month - 1):
            return HttpResponseRedirect(reverse("monthly-challenge", args=[member.name]))
    return HttpResponseNotFound("No month is represented by that number")


def monthly_challenges(request: HttpRequest, month: str) -> HttpResponse:
    try:
        return HttpResponse(MonthlyChallenges.from_name(month).value)
    except ValueError:
        return HttpResponseNotFound("No month with that name exists")

