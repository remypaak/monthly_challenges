from django.shortcuts import render
from helpers.better_enum import BetterEnum
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    Http404
)
from django.urls import reverse
from django.template.loader import render_to_string


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
    december = None


def index(request: HttpRequest) -> HttpResponse:
    month_names = [month.name for month in MonthlyChallenges]
    return render(request, 'challenges/index.html', {
        'month_names': month_names
    })



def monthly_challenge_by_number(request: HttpRequest, month: int):
    for index, member in enumerate(MonthlyChallenges):
        if index == (month - 1):
            return HttpResponseRedirect(reverse("monthly-challenge", args=[member.name]))
    return HttpResponseNotFound("<h1>No month is represented by that number</h1>")


def monthly_challenges(request: HttpRequest, month: str) -> HttpResponse:
    try:
        return render(request, 'challenges/challenge.html', {
            'challenge_of_the_month': MonthlyChallenges.from_name(month).value,
            'month_name': month
                                                             })
    except ValueError:
        raise Http404()

