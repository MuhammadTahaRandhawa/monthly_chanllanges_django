from django.http import HttpRequest, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

all_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

# Create your views here.


def index(request):
    months = list(all_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenges_by_number(request: HttpRequest, month: int):
    if month > 12 or month < 1:
        return HttpResponseNotFound('Invalid month')
    months = list(all_challenges.keys())
    month_string = months[month-1]
    redirected_url = reverse("monthly_challenge_route", args=[month_string])
    return HttpResponseRedirect(redirected_url)


def monthly_challenges(request, month: str):
    try:
        challenge = all_challenges[month]
        return render(request, "challenges/challenge.html", {
            "challenge_text": challenge,
            "month": month
        })
    except:
        raise Http404()

# def show_months(request):
#     try:
#         months = list(all_challenges.keys())

#     except:
