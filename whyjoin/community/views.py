""" Views for the community application """
from django.shortcuts import render


def community(request):
    return render(request, "community.html")
