from django.shortcuts import render


def index(request):
    context = {"ext_from_me": "me"}
    return render(request, 'homepage/index.html', context=context)
